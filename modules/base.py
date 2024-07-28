#!/usr/bin/env python3
"""
base module
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from uuid import uuid4
from datetime import datetime

DB_base = declarative_base()


class Base:
    """
    The base class that will be inherited by all classes
    """

    id = Column(String(45), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, **kwargs):
        """
        the constructor class
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)