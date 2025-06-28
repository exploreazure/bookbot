from stats import get_num_words
from stats import get_char_count
from stats import sort_on
import sys

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# get arguments from the command line
try:
    script_name = sys.argv[0]
    file_name = sys.argv[1]
except IndexError:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

text = get_book_text(file_name)
num_words = get_num_words(text)

def print_sorted_report(sorted_items, num_words):
    """
    Prints a sorted report of items.
    
    Args:
        sorted_items (list): A list of tuples containing items and their counts.
    """
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_name}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print(f'--------- Character Count -------')
    for item, count in sorted_items:
        if(item.isalpha()):
            print(f'{item}: {count}')     
    print('============= END ===============')
    

#print(f'{num_words} words found in the document')

num_words = get_num_words(text)
unique_chars = get_char_count(text)

#print(unique_chars)

sorted_chars = sort_on(unique_chars)

print_sorted_report(sorted_chars,num_words)
