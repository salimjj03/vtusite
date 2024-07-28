#!/usr/bin/env python3
"""
User module
"""

from modules.base import Base, DB_base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey


class User(Base, DB_base):
    """
    user class which inherite from Base and db_base
    """
    __tablename__ = "users"

    full_name = Column(String(45), nullable=False)
    user_name = Column(String(45), unique=True, nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    phone_no = Column(String(15), unique=True, nullable=False)
    ref_id = Column(String(45), ForeignKey("users.user_name"), nullable=False)
    password = Column(String(45), nullable=False)
    balance = Column(Numeric(10), default=0)
    type = Column(String(45), default="type_1", nullable=False)
    accounts = Column(String(255))
    status = Column(String(45), default="un verified")
    pin = Column(Integer)
    accountReference = Column(String(45), unique=True)
    suspended = Column(String(45), default="False")
    bvn = Column(String(15))
