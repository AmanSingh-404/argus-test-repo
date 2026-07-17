def get_user(user_id, include_deleted=False):
    """Fetches a user record by ID from the database."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    if not include_deleted:
        query += " AND deleted_at IS NULL"
    result = db.execute(query)
    return result if result else None
