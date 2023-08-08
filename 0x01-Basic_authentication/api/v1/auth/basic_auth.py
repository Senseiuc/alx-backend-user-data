#!/usr/bin/env python3
"""
Basic_Auth Class: Task 4
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    A basic auth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the base64 authorise header
        :param authorization_header: The authorised header string
        :return: the Base64 part of the Authorization
        """
        if authorization_header and type(authorization_header) == str:
            if authorization_header.startswith('Basic'):
                return authorization_header.split(' ')[1]
        return None
