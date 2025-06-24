import sys
from stats import (
    count_book_words,
    count_book_characters,
    sorted_characters,
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book> Please enter the filepath of the book you want to count.")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = count_book_words(text)
    num_chars = count_book_characters(text)
    report = sorted_characters(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in report:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()