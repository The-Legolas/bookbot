  
def get_num_words(text):
    # This splits the strings up into a list so I can
    # count up the number of words.
    words = text.split()

    # This takes the text-list and splits them so I can count them later
    return len(words)

# This function finds the file with a given filepath
# And then converts it into a string for python to rea#d
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()


def get_count_characters():
    all_characters = get_book_text("books/frankenstein.txt") 
    
    list_of_characters = {}

    for character in list(all_characters.lower()):
        for i in character:
            if i not in list_of_characters:
                list_of_characters[character] = 0
    
    return list_of_characters
