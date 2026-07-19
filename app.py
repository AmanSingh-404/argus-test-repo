def get_user(user_id, include_deleted=False):
    """Fetches a user record by ID from the database."""
    query = "SELECT * FROM users WHERE id = ?"
    
    if not include_deleted:
        query += " AND deleted_at IS NULL"
    
    return result if result else None
