def add_many_numbers(numbers):
    total = 0
    for number in numbers:
        total +=number
     
    return total
    

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = add_many_numbers(numbers)
print(sum_of_numbers)