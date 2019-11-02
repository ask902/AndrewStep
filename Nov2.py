def average(numbers):
    if len(numbers) == 0:
        return 0 
    total = 0
    for num in numbers:
        total += num
    return float(total) / len(numbers)