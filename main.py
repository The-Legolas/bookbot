#This is where the main thing happens
def main():
    text = get_book_text("books/frankenstein.txt")

    # This splits are string up into a list so I can
    # count up the number of words.
    words = text.split()
    
    # This prints the required assignment
    print(f"{len(words)} words found in the document")


# This function finds the file with a given filepath
# And then converts it into a string for python to read
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    


main()
