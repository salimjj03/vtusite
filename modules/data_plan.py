#!/usr/bin/env python3
"""
data plane module
"""

from sqlalchemy import Column, String, ForeignKey, Numeric, Integer
from modules.base import Base, DB_base


class DataPlan(Base, DB_base):
    """
    data plane class
    """

    __tablename__ = "data_plans"

    plan_id = Column(Integer, unique=True, nullable=False)
    plan_size = Column(String(45), ForeignKey("data_plan_sizes.name"), nullable=False)
    plan_name = Column(String(45), ForeignKey("data_plan_names.name"), nullable=False)
    plan_type = Column(String(45), ForeignKey("data_plan_types.name"), nullable=False)
    network_id = Column(Integer, ForeignKey("networks.network_id"), nullable=False)
    user1_price = Column(Numeric(10), nullable=False)
    user2_price = Column(Numeric(10), nullable=False)
    user3_price = Column(Numeric(10), nullable=False)
    user4_price = Column(Numeric(10), nullable=False)
    user5_price = Column(Numeric(10), nullable=False)
    user6_price = Column(Numeric(10), nullable=False)
    validity_days = Column(Integer, nullable=False)
    status = Column(String(45), default="enable", nullable=False)
    commission = Column(Numeric(10), default=1)