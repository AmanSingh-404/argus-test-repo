# API Reference

## get_user(user_id, include_deleted=False)

Fetches a user record by ID from the database.

**Parameters:**
- `user_id` (int) — the user's unique identifier
- `include_deleted` (bool) — whether to include deleted user records (default `False`)

**Returns:** a user dict, or `None` if not found.