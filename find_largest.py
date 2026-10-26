def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [10, 25, 7, 42, 18]

print(find_largest(numbers))
