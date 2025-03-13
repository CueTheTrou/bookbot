import sys
from stats import (
    get_num_words,
    get_num_chars,
    sort_dict,
)
 

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    
    print("============= END ===============")

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_num = get_num_chars(book_text)
    sorted_chars = sort_dict(char_num)
    print_report(filepath, num_words, sorted_chars)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])