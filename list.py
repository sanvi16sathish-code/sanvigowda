numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("First number:", numbers[0])
print("Last number:", numbers[-1])

print("All numbers:")
for n in numbers:
    print(n)

print("Numbers in reverse:")
for n in numbers[::-1]:
    print(n)
