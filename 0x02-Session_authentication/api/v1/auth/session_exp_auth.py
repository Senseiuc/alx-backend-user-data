#!/usr/bin/env python3
"""
Task 10
"""
from datetime import datetime, timedelta

from .session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    A Session Expiration Authentication Class
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION', '0'))
        except TypeError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creates a session
        :param user_id: The user_id of the session to be
        created
        :return: the session id created
        """
        session_id = super().create_session(user_id)
        if type(session_id) != str:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        A function that gets the userid of a session id
        :param session_id: the session id
        :return: the user id
        """
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' in session_dict:
                cur_time = datetime.now()
                session_time = timedelta(seconds=self.session_duration)
                expiration_time = session_dict['created_at'] + session_time
                if cur_time > expiration_time:
                    return session_dict['user_id']
