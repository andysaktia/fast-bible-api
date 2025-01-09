# Bible API

A simple and efficient API to access Bible verses, chapters, and books. This project showcases how to structure a FastAPI project while implementing token-based authentication and a JSON data-driven backend.

## Features

- Retrieve Bible data by book, chapter, and verse.
- Token-based authentication for secure API access.
- Clear and well-structured JSON responses.
- Pagination support for large data sets.
- Easy-to-use endpoints for developers.

## Project Structure

```plaintext
project/
├── app/
│   ├── __init__.py       # Marks directory as a Python module
│   ├── main.py           # Entry point of the application
│   ├── routers/          # Contains API route definitions
│   │   ├── __init__.py
│   │   ├── bible.py      # Routes for Bible-related endpoints
│   ├── models/           # Data models and schema definitions
│   │   ├── __init__.py
│   │   ├── bible.py      # Pydantic models for Bible data
│   ├── utils/            # Utility functions and helpers
│       ├── __init__.py
│       ├── helpers.py    # Helper functions for data operations
│       ├── auth.py       # Authentication-related logic
├── data/
│   ├── bible.json        # JSON file containing Bible data
├── tests/                # Unit tests
│   ├── __init__.py
│   ├── test_main.py      # Integration tests for API
│   ├── test_bible.py     # Tests for Bible API
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
├── .gitignore            # Ignored files and directories for Git
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bible-api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bible-api
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

5. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

### Get a specific verse
```http
GET /bible/{book_identifier}/{chapter}/{verse}
```
#### Parameters:
- `book_identifier` (string): The book ID or name (e.g., `Genesis` or `Gen`).
- `chapter` (integer): The chapter number.
- `verse` (integer): The verse number.

#### Example:
```bash
curl -X GET "http://127.0.0.1:8000/bible/Genesis/1/1" \
-H "Authorization: your-secret-token"
```

```powershell
curl.exe -X GET "http://127.0.0.1:8000/bible/Genesis/1/1" -H "Authorization: Bearer your-secret-token"
```

#### Response:
```json
{
  "book_id": "Gen",
  "book_name": "Genesis",
  "chapter": 1,
  "verse": 1,
  "text": "In the beginning God created the heaven and the earth.",
  "translation_id": "KJV"
}
```

### Get all verses in a chapter
```http
GET /bible/{book_identifier}/{chapter}
```
#### Example:
```bash
curl -X GET "http://127.0.0.1:8000/bible/Genesis/1" \
-H "Authorization: your-secret-token"
```

### Get all verses in a book
```http
GET /bible/{book_identifier}
```
#### Example:
```bash
curl -X GET "http://127.0.0.1:8000/bible/Genesis" \
-H "Authorization: your-secret-token"
```

## Authentication
This API requires a token for authorization. Include the token in the `Authorization` header:
```http
Authorization: your-secret-token
```

## Testing

This project includes automated tests to ensure functionality. Tests are located in the `tests/` directory.

### Running Tests

1. Install `pytest` if not already installed:
   ```bash
   pip install pytest
   ```

2. Run all tests:
   ```bash
   pytest tests/
   ```
   if `pytest tests/` not working try this:
   ```bash
   python -m pytest
   ```

### Test Coverage

- **Unit Tests**: Located in `tests/test_helpers.py`. These validate the functionality of helper functions like `find_verse`.
- **Integration Tests**: Located in `tests/test_main.py`. These test API endpoints using FastAPI's `TestClient`.

Example test command:
```bash
pytest tests/test_helpers.py
pytest tests/test_main.py
```


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any feature additions or bug fixes.

---

Feel free to reach out if you have any questions or suggestions!






