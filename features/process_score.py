from data import state
from classes import User
from store import db_utils
def process_score():
    state.currentScore += 1

    if state.currentScore > state.user['score']:
        db_utils.log_highscore({**state.user, 'score': state.currentScore})
        new_user = db_utils.get_user_db(state.user['username'])
        state.user = new_user