def get_user(user_id):
      if user_id = None:
  return db.query(f"SELECT * FROM users WHERE id={user_id}")
