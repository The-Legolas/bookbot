from stats import get_num_words
from stats import get_book_text
from stats import get_count_characters


#This is where the main thing happens
def main():
    text = get_book_text("books/frankenstein.txt") 
    num_words = get_num_words(text)
    chars_num = get_count_characters(text)


    # This prints the required assignment
    print(f"{num_words} words found in the document")
    print(chars_num)



main()
