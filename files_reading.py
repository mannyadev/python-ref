# python3 files_reading.py files_reading.txt
from sys import argv
script, filename = argv

text = open(filename)

print(f"Reading file: {filename} ...")
print(text.read())

print("Type Filename Again: ")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())
