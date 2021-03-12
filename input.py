print("This exercise is about getting user input from the console ...")

# end=' '   ->  do not end line with newline,
# go to next line

print("How old are you?", end=' ')
age = input()

print("What is your height?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

print(f"You are {age} years old, {height}cm tall and weigh {weight}kg")
