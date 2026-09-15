from operator import itemgetter
from classes import User

def sort_users(users):
    if not users:
        return []
    return sorted(users, key=itemgetter(1), reverse=True)
