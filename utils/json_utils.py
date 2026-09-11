import json
import os
from random_username.generate import generate_username

from store import db_utils
from data import state

USERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'users.json')

def init_user():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            saved = json.load(f)
        user = db_utils.get_user_db(saved['id'])
        if user:
            state.user = user
            return user

    new_user = state.user_empty_state
    db_utils.init_user_db(new_user)
    with open(USERS_FILE, 'w') as f:
        json.dump({'id': new_user['id']}, f)
    state.user = new_user
    return new_user
