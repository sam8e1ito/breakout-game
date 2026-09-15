from .db_init import *
from classes import User
from operator import itemgetter


def get_user_db(username):
    rows = execute_read("SELECT * FROM score WHERE username = ?", (username,))
    if not rows:
        return None
    return dict(rows[0])

def log_highscore(user_data: User):
    username, score = user_data['username'], user_data['score']
    execute_write("UPDATE score SET score = ? WHERE username = ?", (score, username))

def get_users():
    try:
        rows = execute_read("SELECT username, score FROM score ORDER BY score DESC")
        return rows if rows is not None else []
    except Exception as e:
        print(f"DB Error while fetching users: {e}")
        return []
    
def sort_users(users: dict):
    sorted_users = dict(sorted(users.items(), key=itemgetter(1), reverse=True))
    return sorted_users

def delete_user(user):
    execute_write(
        """
        DELETE FROM score WHERE username = ?
        """,
        (user['username'],)
    )
    return True