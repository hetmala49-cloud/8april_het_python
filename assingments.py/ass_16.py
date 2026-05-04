'''Write a Python program to count the occurrences of each word in a given
sentence'''
sentence = input("Enter a sentence: ")

for word in (sentence.split()):
    print(word, ":", sentence.split().count(word))