from coze_coding_dev_sdk.database import Base

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Double, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, text
from sqlalchemy.dialects.postgresql import OID
from typing import Optional
import datetime

from sqlalchemy.orm import Mapped, mapped_column

class HealthCheck(Base):
    __tablename__ = 'health_check'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='health_check_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('now()'))


# ============== 大类数据库 - 路由分发树状结构 ==============

class ScrewDatabase(Base):
    """螺丝数据库 - 专用类"""
    __tablename__ = "screw_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='screw_database_pkey'),
        Index('ix_screw_database_term_name', 'term_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="专有名词")
    sequence_id: Mapped[str] = mapped_column(String(100), nullable=False, comment="序列号")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class CapacitorDatabase(Base):
    """电容数据库 - 电子元件类"""
    __tablename__ = "capacitor_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='capacitor_database_pkey'),
        Index('ix_capacitor_database_term_name', 'term_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="专有名词")
    sequence_id: Mapped[str] = mapped_column(String(100), nullable=False, comment="序列号")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


class CameraDatabase(Base):
    """摄像机数据库 - 视频设备类"""
    __tablename__ = "camera_database"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='camera_database_pkey'),
        Index('ix_camera_database_term_name', 'term_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="专有名词")
    sequence_id: Mapped[str] = mapped_column(String(100), nullable=False, comment="序列号")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'), comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment="更新时间")


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
    Column('min_exec_time', Double(53)),
    Column('max_exec_time', Double(53)),
    Column('mean_exec_time', Double(53)),
    Column('stddev_exec_time', Double(53)),
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
    Column('shared_blk_write_time', Double(53)),
    Column('local_blk_read_time', Double(53)),
    Column('local_blk_write_time', Double(53)),
    Column('temp_blk_read_time', Double(53)),
    Column('temp_blk_write_time', Double(53)),
    Column('wal_records', BigInteger),
    Column('wal_fpi', BigInteger),
    Column('wal_bytes', Numeric),
    Column('jit_functions', BigInteger),
    Column('jit_generation_time', Double(53)),
    Column('jit_inlining_count', BigInteger),
    Column('jit_inlining_time', Double(53)),
    Column('jit_optimization_count', BigInteger),
    Column('jit_optimization_time', Double(53)),
    Column('jit_emission_count', BigInteger),
    Column('jit_emission_time', Double(53)),
    Column('jit_deform_count', BigInteger),
    Column('jit_deform_time', Double(53)),
    Column('stats_since', DateTime(True)),
    Column('minmax_stats_since', DateTime(True))
)


t_pg_stat_statements_info = Table(
    'pg_stat_statements_info', Base.metadata,
    Column('dealloc', BigInteger),
    Column('stats_reset', DateTime(True))
)


class TermMapping(Base):
    __tablename__ = 'term_mapping'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='term_mapping_pkey'),
        Index('ix_term_mapping_sequence_id', 'sequence_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    term_name: Mapped[str] = mapped_column(String(255), nullable=False, comment='专有名词')
    sequence_id: Mapped[str] = mapped_column(String(100), nullable=False, comment='序列号')
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'), comment='创建时间')
    description: Mapped[Optional[str]] = mapped_column(Text, comment='描述信息')
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), comment='更新时间')
