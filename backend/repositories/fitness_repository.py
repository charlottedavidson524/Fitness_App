class FitnessRepository:
    def __init__(self, db):
        self.db = db

    def create_log(self, user_id, log_date, steps, distance, calories):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        # First validate user exists
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            conn.close()
            raise ValueError("Invalid user_id")
        
        # Create log
        cursor.execute("""
            INSERT INTO fitness_logs (user_id, log_date, steps, distance, calories)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, str(log_date), steps, distance, calories))

        conn.commit()
        log_id = cursor.lastrowid
        conn.close()
        return log_id

    def get_logs_by_user(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, log_date, steps, distance, calories
            FROM fitness_logs
            WHERE user_id = ?
        """, (user_id,))

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "log_date": r[1],
                "steps": r[2],
                "distance": r[3],
                "calories": r[4]
            }
            for r in rows
        ]