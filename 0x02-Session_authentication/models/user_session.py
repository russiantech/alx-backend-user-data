#!/usr/bin/env python3
"""UserSession model"""

from models.base import Base
import datetime
import uuid


class UserSession(Base):
    """UserSession model"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize UserSession"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get(
                'session_id', str(uuid.uuid4()))
        self.created_at = datetime.datetime.now()
