def get_user(user_id):
    """Fetches a user record by ID from the database."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
