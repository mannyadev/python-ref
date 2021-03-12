from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}! I'm {script}")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
So in summary, you said {likes} about liking me.
You live in {lives}, sounds like a nice place!
And you have a {computer} computer. Nice chat :)
""")
