import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    # Check command line arguments inside the main function
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    
    # Get sorted characters
    sorted_chars = sort_char_count(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each alphabetical character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()


