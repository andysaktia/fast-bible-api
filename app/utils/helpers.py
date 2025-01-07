import json

def load_bible_data():
    try:
        with open("data/bible.json", "r") as file:
            data = json.load(file)  # Load JSON file
            if not isinstance(data, list):
                raise ValueError("file json harus berupa list of dictionaries")
            return data
    except FileNotFoundError:
        raise RuntimeError("File bible.json tidak ditemukan.")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Format JSON tidak valid: {e}")


# bible_data = load_bible_data()
# print(type(bible_data))  # Harus <class 'list'>
# print(bible_data[:5])    # Lihat 5 entri pertama untuk memastikan format


def find_verse(data, book_identifier, chapter=None, verse=None):
    results = []
    for entry in data:
        if entry["book_id"].lower() == book_identifier.lower() or entry["book_name"].lower() == book_identifier.lower():
            if chapter and verse:
                if entry["chapter"] == int(chapter) and entry["verse"] == int(verse):
                    return entry
            elif chapter:
                if entry["chapter"] == int(chapter):
                    results.append(entry)
            else:
                results.append(entry)
    return results if results else None
