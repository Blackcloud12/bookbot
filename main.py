def main():
    path = "books/frankenstein.txt"
    with open(path) as file:
        file_content = file.read()
        total = word_count(file_content)
        print(f"---Begin report of {path} ---")
        print(f'{total} words found in the document')
        letter_dic = letter_count(file_content)
        for k in letter_dic:
            print(f"The '{k}' character was found {letter_dic[k]} times")
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

# sort dic in decending order

main()