word = str(input("Enter a word: ")).lower()
character = str(input("Enter a character to count: ")).lower()

i = 0
matches = 0

while i < len(word):
    if word[i] == character:
        matches += 1
    i += 1

print(f"The character '{character}' appears {matches} times in the word '{word}'.")


