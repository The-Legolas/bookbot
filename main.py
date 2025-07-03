#This is where the main thing happens
def main():
    # This takes the text-list and splits them so I can count them later
    text = split_words()
    
    # This prints the required assignment
    print(f"{len(text)} words found in the document")


# This function finds the file with a given filepath
# And then converts it into a string for python to rea#d
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def split_words():
    text = get_book_text("books/frankenstein.txt")

    # This splits the strings up into a list so I can
    # count up the number of words.
    words = text.split()
    return words

main()
