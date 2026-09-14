from data import state, constants
from store import db_utils

def generate_guest():
    guest = constants.user_empty_state
    state.user = guest
    db_utils.execute_write(
        """
        INSERT INTO score (id, username, score) VALUES (?, ?, ?)
        """, (guest['id'], guest['username'], guest['score'])
    )
    print(db_utils.execute_read('SELECT * FROM score WHERE username = ?', (guest['username'],)))
