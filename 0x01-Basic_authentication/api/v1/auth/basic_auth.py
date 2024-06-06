#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
import base64
from typing import TypeVar, List, Tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class for handling Basic Authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the
        Authorization header for Basic Authentication
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
            if not user or not user[0].is_valid_password(user_pwd):
                return None
            return user[0]
        except Exception:
            return None
