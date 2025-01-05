from pydantic import BaseModel

class Verse(BaseModel):
    book_id: str
    book_name: str
    chapter: int
    verse: int
    text: str
    translation_id: str
