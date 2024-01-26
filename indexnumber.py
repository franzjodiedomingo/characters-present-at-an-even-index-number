# Ask user to enter a word
user_string = input("Enter a word: ")
# Print characters at even indices using a loop:
for i in range(0, len(user_string), 2):
    print(user_string[i])
# Alternatively, print characters at even indices using string slicing: