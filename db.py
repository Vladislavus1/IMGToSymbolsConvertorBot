import sqlite3
connection = sqlite3.connect("bot_database.db")
cursor = connection.cursor()


def run_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_name TEXT, user_id TEXT)")


def add_user(user_name, user_id):
    cursor.execute("INSERT INTO users (user_name, user_id) VALUES (?, ?)", (user_name, user_id))
    connection.commit()


def get_user(user_id):
    cursor.execute(f"""SELECT * FROM users WHERE user_id = ?""", (user_id,))
    users = cursor.fetchall()
    return users