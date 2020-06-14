import psycopg2


def create_connection():
    try:
        conn = psycopg2.connect(user="viktor", password="password",
                                host="127.0.0.1", port="5432", database="chat_app")
        cursor = conn.cursor()
        return cursor, conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to Postgresql:", error)


def create_tables():
    commands = (
        """
        CREATE TABLE chat (
            username VARCHAR(100) NOT NULL,
            message VARCHAR(255) NOT NULL,
            room INTEGER NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """,
    )

    cur, conn = create_connection()
    for command in commands:
        cur.execute(command)
    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
