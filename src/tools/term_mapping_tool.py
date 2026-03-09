"""
专有名词映射工具
用于查询标准物料映射库，根据专有名词检索对应的序列
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
def search_term_mapping(term_name: str, runtime: ToolRuntime = None) -> str:
    """
    查询专有名词对应的序列号
    
    Args:
        term_name: 专有名词（支持模糊匹配）
    
    Returns:
        返回匹配结果的JSON格式字符串，包含专有名词、序列号等信息
    """
    ctx = runtime.context if runtime else new_context(method="search_term_mapping")
    
    try:
        client = get_supabase_client()
        
        # 模糊查询：查询包含 term_name 的所有记录
        response = client.table('term_mapping').select('*').ilike('term_name', f'%{term_name}%').execute()
        
        if response.data:
            # 按序列号分组，一个序列可能对应多个专有名词
            result_dict: Dict[str, Dict[str, Any]] = {}
            for record in response.data:
                if not isinstance(record, dict):
                    continue
                    
                seq_id = _safe_get(record, 'sequence_id')
                if not seq_id:
                    continue
                    
                if seq_id not in result_dict:
                    result_dict[seq_id] = {
                        'sequence_id': seq_id,
                        'matched_terms': [],
                        'descriptions': []
                    }
                
                term = _safe_get(record, 'term_name')
                if term:
                    result_dict[seq_id]['matched_terms'].append(term)
                
                desc = _safe_get(record, 'description')
                if desc:
                    result_dict[seq_id]['descriptions'].append(desc)
            
            # 转换为列表格式
            results = list(result_dict.values())
            
            logger.info(f"Query successful for term '{term_name}': found {len(results)} sequences")
            return f"查询成功，找到 {len(results)} 个序列匹配：{results}"
        else:
            logger.warning(f"No matches found for term '{term_name}'")
            return f"未找到与专有名词 '{term_name}' 匹配的序列，请检查输入是否正确或联系管理员补充映射库数据"
            
    except Exception as e:
        error_msg = f"查询专有名词映射时出错: {str(e)}"
        logger.error(error_msg)
        return error_msg


@tool
def add_term_mapping(term_name: str, sequence_id: str, description: str = "", runtime: ToolRuntime = None) -> str:
    """
    添加专有名词与序列的映射关系
    
    Args:
        term_name: 专有名词
        sequence_id: 序列号
        description: 描述信息（可选）
    
    Returns:
        操作结果
    """
    ctx = runtime.context if runtime else new_context(method="add_term_mapping")
    
    try:
        client = get_supabase_client()
        
        # 检查是否已存在相同的映射
        existing = client.table('term_mapping').select('*').eq('term_name', term_name).eq('sequence_id', sequence_id).execute()
        
        if existing.data:
            return f"映射关系已存在：专有名词 '{term_name}' -> 序列 '{sequence_id}'"
        
        # 插入新记录
        response = client.table('term_mapping').insert({
            'term_name': term_name,
            'sequence_id': sequence_id,
            'description': description
        }).execute()
        
        logger.info(f"Successfully added mapping: {term_name} -> {sequence_id}")
        return f"成功添加映射关系：专有名词 '{term_name}' -> 序列 '{sequence_id}'"
        
    except Exception as e:
        error_msg = f"添加映射关系时出错: {str(e)}"
        logger.error(error_msg)
        return error_msg
