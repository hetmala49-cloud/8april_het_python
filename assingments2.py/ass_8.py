#13
#Write a Python program to convert a list of characters into a string.

def convert_to_string(char_list):
    return ''.join(char_list)

characters = []

n = int(input("Enter the number of characters: "))

for _ in range(n):
    char = input("Enter a character: ")
    characters.append(char)

result = convert_to_string(characters)
print("Converted string:", result)