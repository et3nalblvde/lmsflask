import sqlite3


DB_NAME = "database.db"


CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL,
    city_from TEXT NOT NULL
);
"""

CREATE_WORKS_TABLE = """
CREATE TABLE IF NOT EXISTS works (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    score INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""


USERS_DATA = [
    ("Иван Иванов", "ivan@example.com", 30, "Москва"),
    ("Анна Петрова", "anna@example.com", 25, "Санкт-Петербург"),
    ("Сергей Смирнов", "sergey@example.com", 40, "Новосибирск"),
    ("Мария Васильева", "maria@example.com", 22, "Екатеринбург"),
    ("Дмитрий Кузнецов", "dmitry@example.com", 35, "Казань"),
]

WORKS_DATA = [
    ("Исследование Марса", "Работа о геологии Марса", 18, 1),
    ("Биология в космосе", "Эксперименты с растениями", 20, 2),
    ("Физика невесомости", "Влияние невесомости на материалы", 15, 3),
    ("Колонизация Луны", "Проект поселения на Луне", 19, 4),
    ("Новая энергетика", "Развитие ядерной энергетики", 17, 5),
]


def create_and_seed_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_WORKS_TABLE)


    cursor.executemany("INSERT INTO users (name, email, age, city_from) VALUES (?, ?, ?, ?)", USERS_DATA)
    conn.commit()


    cursor.executemany("INSERT INTO works (title, description, score, user_id) VALUES (?, ?, ?, ?)", WORKS_DATA)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_seed_db()

