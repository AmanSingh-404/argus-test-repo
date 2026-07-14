def get_user(user_id):
    if user_id = None:  # note: single = instead of ==, both a logic bug AND could mask an auth bypass
        return db.query(f"SELECT * FROM users WHERE id={user_id}")
