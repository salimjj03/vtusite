#!/usr/bin/env python3
"""
plan size modules
"""

from sqlalchemy import Column, String, Integer
from modules.base import Base, DB_base


class Network(Base, DB_base):
    """
    plan size  class
    """

    __tablename__ = "networks"

    network_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(45), unique=True, nullable=False)