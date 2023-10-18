def replace_missing_element(numbers):
    index_none = numbers.index(None)
    numbers[index_none]=0
    total_sum = sum(numbers)
    total_count = len(numbers)
    
    average = total_sum / total_count
    numbers[index_none] = average
    
    return numbers

numbers = [1, 2, 3, None, 5]
result = replace_missing_element(numbers)
print(result)
