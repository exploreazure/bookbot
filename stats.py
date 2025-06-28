# File: stats.py   
def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_char_count(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        int: The number of characters in the text.
    """

    unique_chars = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in unique_chars.keys():
            unique_chars[lower_char] += 1
        else:
            unique_chars[lower_char] = 1
    return unique_chars


def sort_on(items): 
    """
    Sorts a dictionary by its values in descending order.
        
    Args:
        items (dict): The dictionary to sort.
            
    Returns:
        list: A list of tuples sorted by value in descending order.
    """

    sorted_items = sorted(items.items())
    return sorted_items  


    