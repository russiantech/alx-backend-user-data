#!/usr/bin/env python3
"""
Module for the Auth class
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth class for managing API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
