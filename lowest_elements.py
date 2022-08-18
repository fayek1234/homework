

numbers = [198, 3, 4, 9, 10, 9, 2]

print(f"Number: {numbers}")

first = 10
second = 10

for number in numbers:
    if number < first:
        second = first
        first = number

    elif number > first and number < second:
        second = number


print(f"first: {first}")
print(f"Second: {second}")