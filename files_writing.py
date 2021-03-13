from sys import argv
script, filename = argv

# clear file if necessary
print(f"Erase file {filename}?")
print("""
CTRL-C (^C) to cancel
RETURN to proceed
""")
input("?")

# opens file in 'write' mode
print("Opening the file ...")
target = open(filename,'w')

# empties file
print("Truncating the file. Goodbye!")
target.truncate()

# get input
print("Enter 3 lines of input ...")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Writing to file ...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing file.")
target.close()
