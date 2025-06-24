def count_book_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_book_characters(file_contents):
    chars = file_contents.lower()
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

def sorted_characters(file_contents):
    sorted_chars = []
    def sort_method(dicts):
        return dicts["num"]
    for char_key in file_contents:
        if char_key.isalpha():
            char_count = {"char":char_key, "num":file_contents[char_key]}
            sorted_chars.append(char_count)
    sorted_chars.sort(reverse=True, key=sort_method)
    return sorted_chars