input_string = "saanvi sathish"
unique_chars = []

for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)

print("unique characters without using set:", unique_chars)