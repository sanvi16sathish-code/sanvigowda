text = input("Enter a string: ")

for char in set(text):
    print(f"{char}: {text.count(char)}")
