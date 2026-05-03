from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tehtävien ja kategorioiden SQL-tietokantataulut."""
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists Tasks;
    ''')

    cursor.execute('''
        drop table if exists Categories;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tehtävien ja kategorioiden SQL-tietokantataulut."""
    cursor = connection.cursor()

    cursor.execute('''
        create table Tasks (
            id integer primary key,
            title text,
            date date,
            completed integer,
            category_id references Categories
        );
    ''')

    cursor.execute('''
        create table Categories (
            id integer primary key,
            title text
        );
    ''')
    connection.commit()


def initialize_database():
    """Alustaa sovelluksen SQL-tietokantataulut."""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
