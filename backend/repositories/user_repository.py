class UserRepository:
    def __init__(self, db):
        self.db = db

    # Create a row in the user database
    def create_user(self, username, password_hash, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO users (username, password_hash, email)
                VALUES (?, ?, ?)
            """, (username, password_hash, email))
            conn.commit()
            return cursor.lastrowid

        except conn.IntegrityError:
            raise ValueError("Username already exists")
        
        finally:
            conn.close()

    # Reading a row in the user database
    def get_user_by_username(self, username):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, password_hash, email
            FROM users
            WHERE username = ?
        """, (username,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "id": row[0],
                "username": row[1],
                "password_hash": row[2],
                "email": row[3]
            }
        
        return None