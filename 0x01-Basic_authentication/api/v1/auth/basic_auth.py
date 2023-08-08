#!/usr/bin/env python3
"""
Basic_Auth Class: Task 4
"""
import base64
import binascii
from typing import TypeVar
from models.user import User

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
        b = base64_authorization_header
        if b and type(b) == str:
            try:
                res = base64.b64decode(b)
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        A function that extracts user credentials
        :param decoded_base64_authorization_header: the string that the
               username and pass is extracted
        :return: a tuple of two strings
        """
        d = decoded_base64_authorization_header
        if d and type(d) == str and ':' in d:
            try:
                username, password = tuple(d.split(':', 1))
                return username, password
            except IndexError:
                return None, None
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Retrieves a user based on the user's authentication credentials.
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
