  
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
   


def get_count_characters(text):
    
    list_of_characters = {}
    
    for character in text.lower():
        if character not in list_of_characters:
            list_of_characters[character] = 1
        else:
            list_of_characters[character] += 1
    new_list = []

    for char, num in list_of_characters.items():
        new_list.append({"char": char, "num": num})
    return new_list

def sort_on(items):
    return items["num"]