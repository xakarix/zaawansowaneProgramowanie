def multiply_i(numbers: list):
    new_list = []
    for num in numbers:
        new_list.append(num * 2)

    return new_list

def multiply_ii(numbers: list):
    return [num * 2 for num in numbers]

nums = range(1,11)

print(multiply_i(nums))
print(multiply_ii(nums))