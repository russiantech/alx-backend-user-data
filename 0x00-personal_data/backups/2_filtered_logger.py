#!/usr/bin/env python3
"""
Module that defines a function to obfuscate PII data in a log message, a
RedactingFormatter class to format log messages, and a function to create
a logger.
"""

import re
import logging
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, redacting sensitive information.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log record with sensitive information redacted.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    Creates a logger object named "user_data".

    The logger should only log up to logging.INFO level and should not
    propagate messages to other loggers. It should have a StreamHandler with
    RedactingFormatter as formatter.

    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
