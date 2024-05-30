#!/usr/bin/env python3

"""
Encrypt Password Module

This module provides functionality for hashing passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password: The password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Generate a salt and hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password matches its hashed version.

    Args:
        hashed_password: The hashed password.
        password: The password to check.

    Returns:
        bool: True if the password matches the hashed version, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
