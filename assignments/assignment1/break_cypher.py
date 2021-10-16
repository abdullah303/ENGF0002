import enchant # spellchecking library

d = enchant.Dict("en_UK")
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def shift_letters(word, shift):
    newWord = ""
    for i in word.upper():
        if alphabet.index(i) + shift > 25:
            newWord = newWord + alphabet[alphabet.index(i) + shift - 26]
        else:
            newWord = newWord + alphabet[alphabet.index(i) + shift]
    return newWord

def break_cypher(text):
    for i in range(26):
        word = shift_letters(text, i + 1)
        if d.check(word):
            print("The offset is", i + 1, "and the decoded string is", word)
            return i
