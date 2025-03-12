# CIS-117 Lab2
# Write a description of your module here
# Group#
# Names of all group members (first and last)

def palindrome(word) -> bool:
    return word == word[::-1]

def pangram(sentence) -> bool:
    return len(set(filter(str.isalpha, sentence.lower()))) == 26

def tautogram(sentence) -> bool:
    sentence = sentence.lower()
    words = sentence.split(" ")
    first_word = words[0][0]  
    for i in range(1, len(words)):  
        word = words[i]
        if word[0] != first_word:  
            return False  
    return True  


    
