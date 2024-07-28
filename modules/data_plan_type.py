#!/usr/bin/env python3
"""
plan size modules
"""

from sqlalchemy import Column, String
from modules.base import Base, DB_base


class DataPlanType(Base, DB_base):
    """
    plan size  class
    """

    __tablename__ = "data_plan_types"

    name = Column(String(45), unique=True, nullable=False)