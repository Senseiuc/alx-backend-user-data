#!/usr/bin/env python3
"""
Basic_Auth Class: Task 4
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    A basic auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the base64 authorise header
        :param authorization_header: The authorised header string
        :return: the Base64 part of the Authorization
        """
        if authorization_header and type(authorization_header) == str:
            if authorization_header.startswith('Basic'):
                try:
                    return authorization_header.split(' ')[1]
                except IndexError:
                    return None
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        A function that decodes a base64 authorised header
        :param base64_authorization_header: a base64 string
        :return: the decoded value of the Base64 string
        """
        if base64_authorization_header and type(base64_authorization_header) == str:
            base64_authorization_header.decode('utf-8')
        return None
