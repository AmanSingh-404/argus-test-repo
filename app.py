def get_user(user_id):
    """Fetches a user record by ID, or raises UserNotFoundError if no match exists."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    if not result:
        raise UserNotFoundError(f"No user with id {user_id}")
    return result


# test again solve the github response webhook problem
# fix the self check prompt and test again
# make more better change toke o/p limit 1024 to 2048
