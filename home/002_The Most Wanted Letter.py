"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter
in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you
do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
"""

def checkio(str):

    #replace this for solution
    total = 0
    lower = str.lower()
    most = lower[0]
    for i in lower:
        if i.isalpha():
            if lower.count(i) > total:
                most = i
                total = lower.count(i)
            elif lower.count(i) == total:
                if i < most:
                    most = i
                    total = lower.count(i)
    return most

"""
unable to address the problem of same max value
    import re
    newstring = re.sub(r'\W+', '', str)
    newstring = newstring.lower()
    counts = {}
    for letter in newstring:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return max(counts, key=counts.get)  
"""    
    
  

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

"""
Best Solution 1
"""

import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


"""
Best Solution 2

letter_count = {'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 3}
max(sorted(letter_count), key=letter_count.get)
'l'
"""

def checkio(text):
    letters = [ch for ch in text.lower() if ch.isalpha()]
    letter_count = {ch: letters.count(ch) for ch in set(letters)}
    return max(sorted(letter_count), key=letter_count.get)
