def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
