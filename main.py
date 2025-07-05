#This is where the main thing happens
def main():
    text = get_book_text("books/frankenstein.txt") 
    num_words = get_num_words(text)

    # This prints the required assignment
    print(f"{num_words} words found in the document")


# This function finds the file with a given filepath
# And then converts it into a string for python to rea#d
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def get_num_words(text):
    # This splits the strings up into a list so I can
    # count up the number of words.
    words = text.split()

    # This takes the text-list and splits them so I can count them later
    return len(words)

main()
