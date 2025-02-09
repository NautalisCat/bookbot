def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    print(len(words))

def times_appears():
    number_of_chars = {}
    count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lowered_string = file_contents.lower()

    for char in lowered_string:
        if char in number_of_chars:
            number_of_chars[char] += 1
        else:
            number_of_chars[char] = 1
    return number_of_chars

answer = times_appears()
print(answer)


