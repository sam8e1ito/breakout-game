from store import db_utils
from data import constants, state

class User:
    def __init__(self, username: str, score: int = 0):
        self.username = username
        self.score = score

    def __repr__(self):
        return f"User(username={self.username!r}, score={self.score})"
    
    def save_score(self, new_score: int):
        state.currentScore += new_score
        db_utils.log_highscore({'username': state.user['username'], 'score': state.user['score']})