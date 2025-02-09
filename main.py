def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    output = len(words)
    print (f"{output} words found in the document")

def times_appears():
    number_of_chars = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lowered_string = file_contents.lower()

    for char in lowered_string:
        number_of_chars[char] = number_of_chars.get(char, 0) + 1
        
    return number_of_chars
def dict_to_list(dict):
    count = 0
    temp_list = []
    for items in dict:
        if items.isalpha():
            print(f"The '{items}' character was found {dict[items]} times")
        #temp_list.append({items:dict[items]})
    return temp_list

main()
post = times_appears()
dict_to_list(post)


