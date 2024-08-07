#!/usr/bin/env python3
"""
Admin module
"""

from modules.base import Base, DB_base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey


class Admin(Base, DB_base):
    """
    user class which inherite from Base and db_base
    """
    __tablename__ = "admins"

    full_name = Column(String(45), nullable=False)
    user_name = Column(String(45), unique=True, nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    phone_no = Column(String(15), unique=True, nullable=False)
    password = Column(String(45), nullable=False)
    type = Column(String(45), default="type_1", nullable=False)
