from coze_coding_dev_sdk.database import Base

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Double, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, text
from sqlalchemy.dialects.postgresql import OID
from typing import Optional
import datetime

from sqlalchemy.orm import Mapped, mapped_column


# ============== 大类数据库 - 路由分发树状结构 ==============

class PoleDatabase(Base):
    """杆塔数据库 - 域=ELE, 类码=POL"""
    __tablename__ = "pole_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pole_database_pkey'),
        Index('ix_pole_database_term_name', 'term_name'),
        Index('ix_pole_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class CrossarmDatabase(Base):
    """横担与铁附件数据库 - 域=ELE, 类码=IRO"""
    __tablename__ = "crossarm_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='crossarm_database_pkey'),
        Index('ix_crossarm_database_term_name', 'term_name'),
        Index('ix_crossarm_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class InsulatorDatabase(Base):
    """绝缘子数据库 - 域=ELE, 类码=INS"""
    __tablename__ = "insulator_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='insulator_database_pkey'),
        Index('ix_insulator_database_term_name', 'term_name'),
        Index('ix_insulator_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class FittingDatabase(Base):
    """电力金具数据库 - 域=ELE, 类码=FIT"""
    __tablename__ = "fitting_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='fitting_database_pkey'),
        Index('ix_fitting_database_term_name', 'term_name'),
        Index('ix_fitting_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class GuyWireDatabase(Base):
    """拉线材料数据库 - 域=ELE, 类码=GUY"""
    __tablename__ = "guy_wire_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='guy_wire_database_pkey'),
        Index('ix_guy_wire_database_term_name', 'term_name'),
        Index('ix_guy_wire_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class FastenerDatabase(Base):
    """通用紧固件数据库 - 域=ELE, 类码=FAS"""
    __tablename__ = "fastener_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='fastener_database_pkey'),
        Index('ix_fastener_database_term_name', 'term_name'),
        Index('ix_fastener_database_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(Text, nullable=False, comment="名称（必填）")
    sequence_id: Mapped[str] = mapped_column(Text, nullable=False, comment="序列号（必填），格式：域简称-类码-属码-版本/规格-流水号")
    synonyms: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''::text"), comment="同义词（必填）")
    guide_price: Mapped[Optional[str]] = mapped_column(Text, comment="指导价（非必填）")
    market_price: Mapped[Optional[str]] = mapped_column(Text, comment="市场价（非必填）")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


# ============== 系统表 ==============

class HealthCheck(Base):
    __tablename__ = 'health_check'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='health_check_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'))


t_pg_stat_statements = Table(
    'pg_stat_statements', Base.metadata,
    Column('userid', OID),
    Column('dbid', OID),
    Column('toplevel', Boolean),
    Column('queryid', BigInteger),
    Column('query', Text),
    Column('plans', BigInteger),
    Column('total_plan_time', Double(53)),
    Column('min_plan_time', Double(53)),
    Column('max_plan_time', Double(53)),
    Column('mean_plan_time', Double(53)),
    Column('stddev_plan_time', Double(53)),
    Column('calls', BigInteger),
    Column('total_exec_time', Double(53)),
    Column('min_exec_time', Double(53),
    Column('max_exec_time', Double(53),
    Column('mean_exec_time', Double(53),
    Column('stddev_exec_time', Double(53),
    Column('rows', BigInteger),
    Column('shared_blks_hit', BigInteger),
    Column('shared_blks_read', BigInteger),
    Column('shared_blks_dirtied', BigInteger),
    Column('shared_blks_written', BigInteger),
    Column('local_blks_hit', BigInteger),
    Column('local_blks_read', BigInteger),
    Column('local_blks_dirtied', BigInteger),
    Column('local_blks_written', BigInteger),
    Column('temp_blks_read', BigInteger),
    Column('temp_blks_written', BigInteger),
    Column('shared_blk_read_time', Double(53)),
    Column('shared_blk_write_time', Double(53),
    Column('local_blk_read_time', Double(53),
    Column('local_blk_write_time', Double(53),
    Column('temp_blk_read_time', Double(53),
    Column('temp_blk_write_time', Double(53)),
    Column('wal_records', BigInteger),
    Column('wal_fpi', BigInteger),
    Column('wal_bytes', Numeric),
    Column('jit_functions', BigInteger),
    Column('jit_generation_time', Double(53),
    Column('jit_inlining_count', BigInteger),
    Column('jit_inlining_time', Double(53),
    Column('jit_optimization_count', BigInteger),
    Column('jit_optimization_time', Double(53),
    Column('jit_emission_count', BigInteger),
    Column('jit_emission_time', Double(53),
    Column('jit_deform_count', BigInteger),
    Column('jit_deform_time', Double(53),
    Column('stats_since', DateTime(True)),
    Column('minmax_stats_since', DateTime(True))
)


t_pg_stat_statements_info = Table(
    'pg_stat_statements_info', Base.metadata,
    Column('dealloc', BigInteger),
    Column('stats_reset', DateTime(True))
)
