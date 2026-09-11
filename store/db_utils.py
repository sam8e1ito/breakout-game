from .db_init import *

def get_user_db(user_id): # returns the dict of a user
    rows = execute_read("SELECT * FROM score WHERE id = ?", (user_id,))
    if not rows:
        return None
    return dict(rows[0])

def init_user_db(user):
    execute_write(
        """
        INSERT INTO score(id, username, score)
        VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            username = excluded.username,
            score = excluded.score
        """,
        (user['id'], user['username'], user['score'])
    )

def log_highscore(user_data):
    id, username, score = user_data['id'], user_data['username'], user_data['score']
    execute_write("UPDATE score SET username = ?, score = ? WHERE id = ?", (username, score, id))
