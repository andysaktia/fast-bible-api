# FastBibleAPI  

**FastBibleAPI** is a RESTful API built with **FastAPI**, providing fast and easy access to Bible data. This project supports searching for specific verses, chapters, or entire books of the Bible using filters based on book identifiers, chapters, and verses. It is ideal for religious applications, research projects, or educational platforms.

## Key Features  
- **Verse Lookup**: Retrieve specific verses by book, chapter, and verse numbers.  
- **Chapter Search**: Fetch all verses within a specific chapter.  
- **Book Search**: Access all verses within a specific book of the Bible.  
- **API Security**: Secure API access with token-based authentication.  
- **JSON Data Support**: Bible data is sourced from a JSON file, making it easy to modify or extend.  

## Technologies Used  
- **FastAPI**: A modern, fast web framework for building APIs with Python.  
- **Uvicorn**: A fast and lightweight ASGI server for running the application.  
- **Pytest**: A robust testing framework to ensure API reliability.  

## Project Goals  
This project is designed as an open-source showcase to demonstrate the use of FastAPI for building modern Bible APIs. With a well-structured architecture and comprehensive usage guide, it is perfect for developers who want to learn or implement similar APIs.  

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






