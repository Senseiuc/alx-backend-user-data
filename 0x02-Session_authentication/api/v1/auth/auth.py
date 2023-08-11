#!/usr/bin/env python3
"""
Auth Class: Task 3
"""
import os
from typing import List, TypeVar

from flask import request


class Auth:
    """
    a class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the required auth is given
        :param path: A string represent a path
        :param excluded_paths: a list of paths
        :return: False if path is in the excluded_paths list
        """
        if path is None or excluded_paths in [None, []]:
            return True
        for value in excluded_paths:
            if value.startswith(path):
                return False
            if value[-1] == '*' and path.startswith(value[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Checks for authorisation header
        :param request: a request object
        :return:
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user
        :param request:
        :return:
        """
        return None

    def session_cookie(self, request=None):
        """
        A function that returns the cookie value from
        a request
        :param request: the request object
        :return: the value of the cookie in the request
        """
        if request is not None:
            _my_session_id = os.getenv('SESSION_NAME')
            return request.cookies.get(_my_session_id)
