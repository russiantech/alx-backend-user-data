#!/usr/bin/env python3
"""Session Expiration Authentication"""

import datetime
from api.v1.auth.session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    def __init__(self):
        """Initialize the SessionExpAuth class"""
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION", 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session with an expiration time"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Get user ID from session ID considering session expiration"""
        if session_id is None:
            return None
        
        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None
        
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        
        created_at = session_dict.get("created_at")
        if not created_at:
            return None
        
        if created_at + datetime.timedelta(
                seconds=self.session_duration) < datetime.datetime.now():
            return None
        
        return session_dict.get("user_id")
