

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #words = wordlist(file_contents)
        #print(file_contents)
        #print("wordcount = " + str(wordcount(words)))
        #conver_to_dict(file_contents)
        report(conver_to_dict(file_contents))

def wordcount(list):
    return len(list)

def wordlist(file_contents):
    return file_contents.split()

def conver_to_dict(file_contents):
    lowered = file_contents.lower()
    lowered_list = list(lowered)
    char_dict = {}
    for letter in lowered_list:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def report(char_dict):

    for char in char_dict:
        if char.isalpha() == True:
            print("The '" + str(char) + "' was found " + str(char_dict[char]) + " times")


main()