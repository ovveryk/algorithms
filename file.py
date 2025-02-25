import math

def product_numbers(file):
    numbers = list(map(int, file.read().split()))

    product = math.prod(numbers)

    result = open("result.txt", "w")
    result.write(str(product))
    result.close()

file = open("data.txt")
product_numbers(file)