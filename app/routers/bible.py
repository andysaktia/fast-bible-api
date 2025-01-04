from fastapi import APIRouter, HTTPException, Depends
from app.utils.helpers import load_bible_data, find_verse
from app.utils.auth import validate_token

router = APIRouter()

bible_data = load_bible_data()

# Endpoint untuk book, chapter, dan verse
@router.get("/bible/{book_identifier}/{chapter}/{verse}")
def get_verse(book_identifier: str, chapter: int, verse: int, token: str = Depends(validate_token)):
    result = find_verse(bible_data, book_identifier, chapter, verse)
    if not result:
        raise HTTPException(status_code=404, detail="Verse not found")
    return {
        "book_id": result["book_id"],
        "book_name": result["book_name"],
        "chapter": result["chapter"],
        "verse": result["verse"],
        "text": result["text"],
        "translation_id": result["translation_id"]
    }

# Endpoint untuk book dan chapter tanpa verse
@router.get("/bible/{book_identifier}/{chapter}")
def get_chapter(book_identifier: str, chapter: int, token: str = Depends(validate_token)):
    result = find_verse(bible_data, book_identifier, chapter)
    if not result:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return {
        "book_id": result[0]["book_id"],
        "book_name": result[0]["book_name"],
        "chapter": result[0]["chapter"],
        "verses": [{"verse": entry["verse"], "text": entry["text"]} for entry in result]
    }

# Endpoint untuk book saja
@router.get("/bible/{book_identifier}")
def get_book(book_identifier: str, token: str = Depends(validate_token)):
    result = find_verse(book_identifier)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return {
        "book_id": result[0]["book_id"],
        "book_name": result[0]["book_name"],
        "verses": [{"chapter": entry["chapter"], "verse": entry["verse"], "text": entry["text"]} for entry in result]
    }
