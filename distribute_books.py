import csv
import json
import random
from pathlib import Path

# Пути считаем от самого файла, чтобы скрипт работал из любой папки
BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "files" / "users.json"
BOOKS_FILE = BASE_DIR / "files" / "books.csv"
RESULT_FILE = BASE_DIR / "users_with_books.json"


def load_users(path=USERS_FILE):
    """Читает users.json и оставляет только нужные поля + пустой список книг."""
    with open(path, "r", encoding="utf-8") as f:
        users = json.load(f)

    return [
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
        for user in users
    ]


def load_books(path=BOOKS_FILE):
    """Читает books.csv и оставляет название, автора, число страниц и жанр."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"],
            }
            for row in reader
        ]


def distribute_books(books, users):
    """Раздаёт книги пользователям по кругу в случайном порядке.

    Каждому достаётся поровну (разница между людьми не больше одной книги).
    Переданные списки не меняются, возвращается новый список пользователей.
    """
    if not users:
        raise ValueError("Нет пользователей, некому раздавать книги")

    shuffled_books = random.sample(books, len(books))
    result = [{**user, "books": []} for user in users]

    for index, book in enumerate(shuffled_books):
        result[index % len(result)]["books"].append(book)

    return result


def save_result(users, path=RESULT_FILE):
    """Сохраняет пользователей с книгами в JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)


def main():
    users = load_users()
    books = load_books()

    users_with_books = distribute_books(books, users)
    save_result(users_with_books)

    print(f"Пользователей: {len(users)}, книг роздано: {len(books)}")
    print(f"Результат сохранён: {RESULT_FILE}")


if __name__ == "__main__":
    main()
