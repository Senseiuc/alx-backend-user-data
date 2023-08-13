#!/usr/bin/env python3
"""
SessionAuth: Task 1
"""
from uuid import uuid4
from .auth import Auth
from models.user import User


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

    def current_user(self, request=None):
        """
        A function that returns a user object using the
        cookie value
        :param request: The request object
        :return:The user object
        """
        session_id = self.session_cookie(request)
        print(session_id, 'session_id')
        user_id = self.user_id_by_session_id.get(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        A function that destroys a session
        :param request: the request object
        :return: True
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
