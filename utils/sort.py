from operator import itemgetter
from classes import User

def sort_users(users):
    if not users:
        return []

    if isinstance(users, list):
        first_item = users[0]

        if isinstance(first_item, dict):
            return sorted(users, key=lambda u: u.get('score', 0), reverse=True)

        elif isinstance(first_item, User):
            return sorted(users, key=lambda u: u.score, reverse=True)

        elif isinstance(first_item, (tuple, list)):
            return sorted(users, key=itemgetter(1), reverse=True)

    return users