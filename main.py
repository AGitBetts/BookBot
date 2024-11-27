def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = get_char_quant(text)
    char_sorted_list = sorted_dict_to_sorted_list(char_count)
    print(f"--- Beginning the report of {book_path} ---")
    print(f"{word_count} words are in this book")
    for item in char_sorted_list:
        if not item["char"].isalpha():  #.isaplha()
            continue
        print(f"The '{item['char']}' character was found {item['num']} times") # Why is the char/num in quotes?

    print("--- End of the report ---")

    

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_quant(text):
    char_dict = {}
    words = text.split()                 # This can be optimised, remove the inital text.split()
    for word in words:                   # It doesnt need to be broken down into each word first
        string = word.lower()            # Less computation through another loop.
        for cha in string:
            if cha in char_dict:
                char_dict[cha] += 1
            else:
                char_dict[cha] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char":char, "num":dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)               #.sort new command
    return sorted_list
 



main()
