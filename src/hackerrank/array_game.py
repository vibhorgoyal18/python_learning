def count_moves(numbers):
    iteration = 0
    while True:
        are_numbers_equal = True
        for i in range(len(numbers) - 1):
            if numbers[i] != numbers[i + 1]:
                are_numbers_equal = False

        if not are_numbers_equal:
            max_number = max(numbers)
            is_max_skipped = False
            for i in range(len(numbers)):
                if numbers[i] != max_number or is_max_skipped:
                    numbers[i] += 1
                    iteration += 1
                else:
                    is_max_skipped = True
        else:
            break
        print(numbers)
    return iteration


print(count_moves([6, 7, 9, 8, 6]))
