def digit_counter(x):
    number = abs(int(x))
    count = 0

    if number == 0 and count == 0:
        return "1"

    while number > 0:
        number = number // 10
        count = count + 1

    return str(count)


result = digit_counter(input("insert number: "))
print(result)

''' using XOR operator'''