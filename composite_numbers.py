# Select numbers below  certain limit
def number_below(num):
    numbers = []
    for i in range(0, num):
        if i < num:
            numbers.append(i)
    return numbers

# Gets the components of a number singly eg. 101 to 1,0,1
def numbers_and_digits(numbers):
    all_num_digits = []
    for num in numbers:
        num_digits = []
        num_digits.append(num)
        while True:
            # Breaks number down to get its components
            a = num % 10
            num_digits.append(a)
            b = num // 10
            if b < 10:
                if b != 0:
                    num_digits.append(b)
                break
            else:
                num = b
        all_num_digits.append(num_digits)
    return all_num_digits

# Checks if number is a composite number
def adjacent_numbers(numbers):
    difference = 0
    valid = False
    for number in numbers:
        if len(number) == 2:
            print(number[0])
        for index in range(len(number)):
            # checks the compnents of the number to see it the number is a composite number
            if 0 < index < len(number) - 1:
                difference = number[index + 1] - number[index]
                if difference == 1 or difference == -1:
                    valid = True
                else:
                    valid = False
                    break
        if valid:
            print(number[0])
            valid = False


user_range = int(input("Enter range of numbers: "))
lower_numbers = number_below(user_range)
number_list = numbers_and_digits(lower_numbers)
print("Separated number components.[number,component(s)]")
print(number_list)
print("Adjacent numbers")
print(adjacent_numbers(number_list))

