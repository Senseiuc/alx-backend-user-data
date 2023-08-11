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
        if type(user_id) == str:
            uuid_str = str(uuid4())
            self.user_id_by_session_id[uuid_str] = user_id
            return uuid_str

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        A function that returns a User ID based on a Session ID
        :param session_id: a user session id
        :return: the user id
        """
        if type(session_id) == str:
            return self.user_id_by_session_id.get(session_id)
