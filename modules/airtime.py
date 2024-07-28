#!/usr/bin/env python3
"""
plan size modules
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from modules.base import Base, DB_base


class Airtime(Base, DB_base):
    """
    plan size  class
    """

    __tablename__ = "airtime"

    name = Column(String(45), unique=True, nullable=False)

    network_id = Column(
        Integer,
        ForeignKey("networks.network_id"),
        unique=True,
        nullable=False
    )

    airtime_type = Column(
        String(45),
        ForeignKey("networks.network_id"),
        unique=True,
        nullable=False
    )
