def get_user(user_id, include_deleted=False):
    """Fetches a user record by ID from the database."""
    query = "SELECT * FROM users WHERE id = ?"
    

    
    result = db.execute(query, (user_id,))
    return result if result else None
