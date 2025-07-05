from stats import get_num_words
from stats import get_book_text
from stats import get_count_characters
from stats import sort_on
import sys


#This is where the main thing happens
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    text = get_book_text(sys.argv[1]) 
    num_words = get_num_words(text)
    chars_num = get_count_characters(text)
    chars_num.sort(reverse=True, key=sort_on) 
    

    
    # This prints the required assignment


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for i in chars_num:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")




main()
