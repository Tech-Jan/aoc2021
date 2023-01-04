with open("input", "r") as f:
    data = f.read().split("\n")

print(data)
counter = 0
a = 0
for line in data:
    number = int(line)
    if number > a:
        counter += 1
        a = number
    else:
        a = number
print(counter)

counter2 = 0
a2 = 0
number = 0
print(data)
for i in range(len(data) - 3):
    number = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
    number2 = int(data[i + 1]) + int(data[i + 2]) + int(data[i + 3])
    if number2 > number:
        counter2 += 1
print(counter2)
