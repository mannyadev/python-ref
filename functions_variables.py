def fruit_bowl(apples, bananas, oranges):
    print(f"Apples: {apples}")
    print(f"Bananas: {bananas}")
    print(f"Oranges: {oranges}")
    print(f"Time for a healthy snack!")

# Give numbers directly
fruit_bowl(10,8,12)

# Pass varaibles
apple = 4
banana = 2
orange = 6
fruit_bowl(apple,banana,orange)

# pass math to function
fruit_bowl(2+3, 3+4, 10-1)

# combine math and variables
fiveDay = 5
fruit_bowl(fiveDay, fiveDay+2, fiveDay-3)
