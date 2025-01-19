def even_num(numbers: list):
    for num in numbers:
        if num % 2 == 0:
            print(num)

even_num(range(1,11))