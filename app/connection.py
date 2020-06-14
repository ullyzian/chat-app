import psycopg2


# conn = psycopg2.connect(user="viktor", password="password",
#                         host="127.0.0.1", port="5432", database="chat_app")


def create_connection():
    try:
        conn = psycopg2.connect(user="tulqubamntpngi", password="c9b2a29b19ee3793f4d96226f0771cf4f239414ede9bb0889dfa39b988c54350",
                                host="ec2-54-247-118-139.eu-west-1.compute.amazonaws.com", port="5432", database="d7tuo8j8i2h2kd")
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
