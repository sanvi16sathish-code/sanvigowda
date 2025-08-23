text = input("Enter some text: ").split()

for word in set(text):
    print(word, ":", text.count(word))
