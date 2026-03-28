from database import get_db


def test_database_connection():
    db = next(get_db())
    assert db is not None, "Database connection failed"
    db.close()


def say_hello():
    print("Hello, World!")


def main():
    print("Hello from sqlalchemy!")


if __name__ == "__main__":
    main()
