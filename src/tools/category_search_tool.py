"""
大类数据库检索工具 - 支持路由分发树状结构
用于根据用户输入路由到正确的大类数据库，并检索专有名词信息
"""
from langchain.tools import tool, ToolRuntime
from coze_coding_utils.runtime_ctx.context import new_context
from storage.database.supabase_client import get_supabase_client
import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _safe_get(record: Dict[str, Any], key: str, default: Any = None) -> Any:
    """安全地从字典中获取值"""
    if isinstance(record, dict):
        return record.get(key, default)
    return default


@tool
def route_database_category(user_input: str, runtime: ToolRuntime = None) -> str:
    """
    根据用户输入判断需要检索的大类数据库类别
    
    Args:
        user_input: 用户输入的查询内容
    
    Returns:
        返回需要检索的大类数据库名称（如：screw_database, capacitor_database, camera_database）
        如果无法判断，返回"unknown"
    """
    ctx = runtime.context if runtime else new_context(method="route_database_category")
    
    # 大类数据库的关键词映射
    category_keywords = {
        "screw_database": ["螺丝", "螺母", "螺栓", "螺柱", "垫圈", "紧固件", "螺纹"],
        "capacitor_database": ["电容", "电容器", "电感", "电感器", "电阻", "电阻器", "电子元件", "半导体"],
        "camera_database": ["摄像机", "摄像头", "相机", "监控", "视频", "镜头", "成像"]
    }
    
    user_input_lower = user_input.lower()
    
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in user_input_lower:
                logger.info(f"Routed to category: {category}")
                return category
    
    logger.warning(f"Could not determine category for input: {user_input}")
    return "unknown"


@tool
def search_category_database(category: str, term_name: str, runtime: ToolRuntime = None) -> str:
    """
    在指定的大类数据库中检索专有名词
    
    Args:
        category: 大类数据库名称（如：screw_database, capacitor_database, camera_database）
        term_name: 要检索的专有名词（支持模糊匹配）
    
    Returns:
        返回匹配结果，包含5个字段：序列号、名称、同义词、指导价、市场价
    """
    ctx = runtime.context if runtime else new_context(method="search_category_database")
    
    try:
        client = get_supabase_client()
        
        # 验证类别是否有效
        valid_categories = ["screw_database", "capacitor_database", "camera_database"]
        if category not in valid_categories:
            return f"错误：未知的数据类别 '{category}'。有效类别为：{', '.join(valid_categories)}"
        
        # 在指定数据库中进行模糊查询
        response = client.table(category).select('*').ilike('term_name', f'%{term_name}%').execute()
        
        if response.data:
            results = []
            for record in response.data:
                if not isinstance(record, dict):
                    continue
                
                # 提取5个字段
                result_item = {
                    '序列号': _safe_get(record, 'sequence_id', ''),
                    '名称': _safe_get(record, 'term_name', ''),
                    '同义词': _safe_get(record, 'synonyms', ''),
                    '指导价': _safe_get(record, 'guide_price', '未设置'),
                    '市场价': _safe_get(record, 'market_price', '未设置')
                }
                results.append(result_item)
            
            logger.info(f"Query successful in {category} for term '{term_name}': found {len(results)} results")
            return f"在 '{category}' 中找到 {len(results)} 条匹配记录：{results}"
        else:
            logger.warning(f"No matches found in {category} for term '{term_name}'")
            return f"在 '{category}' 中未找到与 '{term_name}' 匹配的记录"
            
    except Exception as e:
        error_msg = f"查询大类数据库时出错: {str(e)}"
        logger.error(error_msg)
        return error_msg


@tool
def add_category_record(category: str, term_name: str, sequence_id: str, 
                       synonyms: str = "", guide_price: str = "", 
                       market_price: str = "", runtime: ToolRuntime = None) -> str:
    """
    向指定的大类数据库添加记录
    
    Args:
        category: 大类数据库名称（如：screw_database, capacitor_database, camera_database）
        term_name: 专有名词（必填）
        sequence_id: 序列号（必填），格式：域简称-类码-属码-版本/规格-流水号
        synonyms: 同义词（必填）
        guide_price: 指导价（非必填）
        market_price: 市场价（非必填）
    
    Returns:
        操作结果
    """
    ctx = runtime.context if runtime else new_context(method="add_category_record")
    
    try:
        client = get_supabase_client()
        
        # 验证类别是否有效
        valid_categories = ["screw_database", "capacitor_database", "camera_database"]
        if category not in valid_categories:
            return f"错误：未知的数据类别 '{category}'。有效类别为：{', '.join(valid_categories)}"
        
        # 验证必填字段
        if not term_name or not sequence_id:
            return "错误：'名称'和'序列号'为必填字段"
        
        # 检查是否已存在相同的记录
        existing = client.table(category).select('*').eq('term_name', term_name).execute()
        
        if existing.data:
            return f"记录已存在于 '{category}' 中：名称 '{term_name}' -> 序列号 '{sequence_id}'"
        
        # 插入新记录
        response = client.table(category).insert({
            'term_name': term_name,
            'sequence_id': sequence_id,
            'synonyms': synonyms,
            'guide_price': guide_price,
            'market_price': market_price
        }).execute()
        
        logger.info(f"Successfully added record to {category}: {term_name} -> {sequence_id}")
        return f"成功添加记录到 '{category}'：名称 '{term_name}' -> 序列号 '{sequence_id}'"
        
    except Exception as e:
        error_msg = f"添加记录时出错: {str(e)}"
        logger.error(error_msg)
        return error_msg
