def sum_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return total, average
numbers = [10, 20, 30, 40, 50]
total, average = sum_average(numbers)

if total is not None and average is not None:
    print(f"Sum: {total}")
    print(f"Average: {average}")
else:
    print("The list is empty.")
