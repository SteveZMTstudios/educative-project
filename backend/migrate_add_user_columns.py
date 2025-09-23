import sqlite3
import os


DB_PATH = os.path.join(os.path.dirname(__file__), 'dev.db')


def get_columns(conn):
    cur = conn.execute("PRAGMA table_info('users')")
    return [row[1] for row in cur.fetchall()]


def main():
    if not os.path.exists(DB_PATH):
        print(f"DB file not found at {DB_PATH}, nothing to migrate.")
        return

    conn = sqlite3.connect(DB_PATH)
    cols = get_columns(conn)
    print('Existing columns:', cols)

    to_add = []
    if 'salt' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN salt TEXT DEFAULT ''")
    if 'token' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN token TEXT DEFAULT ''")
    if 'interest_tags' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN interest_tags TEXT DEFAULT '#newuser'")
    if 'registration_time' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN registration_time TEXT")
    if 'last_login_time' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN last_login_time TEXT")
    if 'profile' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN profile TEXT")
    if 'public_key' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN public_key TEXT")
    if 'private_key' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN private_key TEXT")
    if 'type' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN type TEXT DEFAULT 'user'")
    if 'class' not in cols:
        to_add.append("ALTER TABLE users ADD COLUMN class TEXT DEFAULT 'none'")

    for stmt in to_add:
        print('Executing:', stmt)
        conn.execute(stmt)

    conn.commit()
    conn.close()
    print('Migration complete')


if __name__ == '__main__':
    main()
