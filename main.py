def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)


main()
