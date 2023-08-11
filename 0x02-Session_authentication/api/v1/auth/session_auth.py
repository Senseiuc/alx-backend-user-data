#!/usr/bin/env python3
"""
SessionAuth: Task 1
"""
from uuid import uuid4
from .auth import Auth


class SessionAuth(Auth):
    """
    A class that authenticates using session
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session for a user
        :param user_id: the id of the user
        :return: the session id of the user
        """
        if user_id is None or type(user_id) != str:
            return None

        self.user_id_by_session_id[str(uuid4)] = user_id
        return user_id
