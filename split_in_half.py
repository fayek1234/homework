string1 = "bbbbbcaaaaa""aaaaabbbbbc"
# number of words
n = len(string1)
string = string1.upper()

print(n)

if n % 2 == 0:
    string1 = string[0:n //2]
    string2 = string[n // 2:]
    print("First Half of String:", string1)
    print("Second Half of String:", string2)
else:
    string1 = string[0:(n // 2 + 1)]
    string2 = string[(n // 2 + 1):]
    print("First Half of String:", string1)
    print("Second Half of String:", string2)