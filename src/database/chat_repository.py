from src.database.db import get_connection

def save_message(thread_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_messages (thread_id, role, content)
        VALUES (%s, %s, %s)
        """,
        (thread_id, role, content)
    )

    conn.commit()
    cursor.close()
    conn.close()