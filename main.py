from stats import get_number_of_words, character_count, sorted_char_count
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_number_of_words(text)
    characters = character_count(text)
    sorted_chars = sorted_char_count(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
      if char["character"].isalpha():
        print(f"{char["character"]}: {char["count"]}")
    print("============= END ===============")

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
main()