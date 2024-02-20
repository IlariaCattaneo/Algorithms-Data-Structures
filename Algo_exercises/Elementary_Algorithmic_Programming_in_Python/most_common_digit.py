def most_common_digit(n):
    num_str = str(abs(n))
    digit_count = {}
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    # Find the most common digit(s)
    max_count = max(digit_count.values())
    most_common_digits = [int(digit) for digit, count in digit_count.items() if count == max_count]

    # Return the smallest digit among the most common ones
    return min(most_common_digits)

# ex 1
print(most_common_digit(1969))

# ex 2
print(most_common_digit(44272))

# ex 3
print(most_common_digit(36223771538825331723))

# ex 4
print(most_common_digit(0))