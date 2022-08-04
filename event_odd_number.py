


def count_odd_even_numbers(num):
    even_cntr = 0
    odd_cntr = 0
    str_num = str(num)
    for char in str_num:
        if (int(char) % 2 == 0):
            even_cntr += 1
        else:
            odd_cntr += 1
    print("Number of even numbers :", even_cntr)
    print("Number of odd numbers :", odd_cntr)


count_odd_even_numbers(num=34560)





