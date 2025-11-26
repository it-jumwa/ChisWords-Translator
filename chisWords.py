"""
Name: Jaimee Molina
ID: 202514907
Date Created: Thursday 6th November 2025

This program is a language convert tool for Python Primary School students that
converts English words in Chis-words. The purpose of this tool is to help
students develop their understanding of word structure.
"""

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
specialCharacters = "1234567890`~!@#$%^&*()-_=+[]{}\\|;:'\",<>./?"
suffix1 = "ay"
suffix2 = "way"

file = open("inputwords.txt", 'r')
englishWords = file.read()
englishWords = englishWords.split()

for word in reversed(englishWords):
    index = englishWords.index(word)
    # Remove leading and trailing special characters
    filteredWord = word.strip(specialCharacters)

    # If there is an empty string, remove it
    if len(filteredWord) == 0:
        englishWords.remove(word)

    else:
        englishWords[index] = filteredWord

chisWords = []

for word in englishWords:    
    for letter in word:
        if letter in vowels:
            # Case 2: If the first letter is a vowel
            if word.index(letter) == 0:
                chisWord = word + suffix2
                break
            # Case 1: The word has a vowel, and is not the first letter
            else:
                shift = word.index(letter)

                # Move the letters before the vowel to the end of the word
                chisWord = word[shift:] + word[0:shift]
                chisWord += suffix1
                break
        # Case 3: If there are no vowels
        # If all letters have been iterated through
        if len(word) == (word.index(letter) + 1):
            chisWord = word + suffix1

    # After the word has been processed add it to the chisWords list
    chisWords.append(chisWord)

outputFile = open("OutputFile.txt", "w")
for word in chisWords:
    outputFile.write(word + "\n")

file.close()
outputFile.close()
