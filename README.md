# random-book-distribution

Учебный скрипт на Python: работа с файлами JSON и CSV.

Читает список пользователей из `files/users.json` и список книг из `files/books.csv`,
случайно раздаёт книги пользователям поровну и сохраняет результат в `users_with_books.json`.

У пользователя остаются поля `name`, `gender`, `address`, `age` и список `books`.
У книги: `title`, `author`, `pages`, `genre`.

## Запуск

```
python distribute_books.py
```

Внешние библиотеки не нужны, только Python 3.

## Пример результата

```json
{
    "name": "Lolita Lynn",
    "gender": "female",
    "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
    "age": 34,
    "books": [
        {
            "title": "In a Free State",
            "author": "Naipaul, V. S.",
            "pages": 196,
            "genre": "fiction"
        }
    ]
}
```

Книги раздаются случайно, поэтому при каждом запуске результат разный.
