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
        if path is None:
            return True
        if not excluded_paths:
            return True

        # Ensure the path ends with a slash
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
