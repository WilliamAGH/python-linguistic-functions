# CIS-117 Lab 2, Group 5
# This module provides functions for testing word play / linguistic patterns
# (palindromes, pangrams, tautograms, isograms, abecedarian words, and dobloons)
# Lab 2, Group 5
# Names: Finola Miqailla, William Callahan

def palindrome(word) -> bool:
    """Check if word reads the same forwards and backwards."""
    return word == word[::-1]

def pangram(sentence) -> bool:
    """Check if sentence contains all 26 letters of the alphabet."""
    return len(set(filter(str.isalpha, sentence.lower()))) == 26

def tautogram(sentence) -> bool:
    """Check if all words in text start with the same letter."""
    sentence = sentence.lower()
    words = sentence.split(" ")
    first_word = words[0][0]  
    for i in range(1, len(words)):  
        word = words[i]
        if word[0] != first_word:  
            return False  
    return True  

def isogram(word) -> bool:
    """Check if no letter appears more than once."""
    word = word.lower()
    return len(set(word)) == len(word)

def abecedarian(word) -> bool:
    """Check if letters appear in alphabetical order."""
    word = word.lower()
    return word == ''.join(sorted(word))

def dobloon(word) -> bool:
    """Check if every letter appears exactly twice."""
    word = word.lower()
    return all(word.count(char) == 2 for char in set(word))
