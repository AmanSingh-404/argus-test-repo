def get_user(user_id):
    """Fetches a user record by ID, or raises UserNotFoundError if no match exists."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    if not result:
        raise UserNotFoundError(f"No user with id {user_id}")
    return result
