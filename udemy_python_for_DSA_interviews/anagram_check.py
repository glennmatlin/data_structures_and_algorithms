# Anagram Check

originalInput = 'dog'
potentialAnagram = 'god'

def anagram(originalInput, potentialAnagram):
    originalInput = originalInput.replace(' ', '').lower()
    potentialAnagram = potentialAnagram.replace(' ', '').lower()
    
    if len(originalInput) != len(potentialAnagram):
        return False
    
    input_letterCounts = {}
    potential_letterCounts = {}
    
    for letter in originalInput:
        if letter in input_letterCounts:
            input_letterCounts[letter] += 1
        else:
            input_letterCounts[letter] = 1
    
    for letter in potentialAnagram:
        if letter in potential_letterCounts:
            potential_letterCounts[letter] += 1
        else:
            potential_letterCounts[letter] = 1
    
    print(input_letterCounts == potential_letterCounts)
    
anagram(originalInput, potentialAnagram)