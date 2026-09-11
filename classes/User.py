
from store import db_utils
from data import state
from utils import json_utils

class User:
    def __init__(self, user):
        self.id = user['id']
        self.username = user['username']
        self.score = user['score']

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r}, score={self.score})"

    
    @staticmethod
    def init_user():
        user_dict = json_utils.init_user()
        return user_dict

    def update_user(self, newUser):
        state.user = newUser
        db_utils.log_highscore(newUser)

    def get_user(self):
        return db_utils.get_user_db(state.user['id'])
