#!/usr/bin/env python3
"""
Module that defines a function to obfuscate PII data in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replaces the values of specified fields in a log message with a redaction
    string.

    Args:
        fields (List[str]): The fields to be obfuscated.
        redaction (str): The string to replace the field values with.
        message (str): The original log message.
        separator (str): The character that separates the fields in the
        message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)
