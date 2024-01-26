# Ask user to enter a word
user_string = input("Enter a word: ")
print("Original String:", user_string)
# Print characters at even indices using a loop:
print("Printing only even index chars")
for i in range(0, len(user_string), 2):
    print(user_string[i])
# Alternatively, print characters at even indices using string slicing: