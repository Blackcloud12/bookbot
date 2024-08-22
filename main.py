def main():
    path = "books/frankenstein.txt"
    with open(path) as file:
        file_content = file.read()
        total = word_count(file_content)
        print(f"---Begin report of {path} ---")
        print(f'{total} words found in the document')
        letter_dic = letter_count(file_content)
        list_of_letters = sort_on(letter_dic)
        # sort dic in decending order
        for row in reversed(list_of_letters):
            print(f"The '{row[1]}' character was found {row[0]} times")
        print("--- End report ---")

def word_count(inputStr):
    return len(inputStr.split())

def letter_count(inputStr):
    letter_dic = {}
    for letter in inputStr.lower():
        if letter.isalpha():
            if letter in letter_dic:
                letter_dic[letter] += 1
            else:
                letter_dic[letter] = 1
    return letter_dic

def sort_on(letter_dict):
    list_of_tuples = []
    for pair in letter_dict.items():
        list_of_tuples.append((pair[1],pair[0]))
    list_of_tuples.sort()
    return list_of_tuples

main()