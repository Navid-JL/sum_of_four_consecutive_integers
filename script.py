sum_of_consecutive_integers = int(input('Enter the sum: '))


def find_four_cons_integers(initial_integer, increment_value, sum_of_cons_integers):
    list_of_integers = []
    while initial_integer < sum_of_cons_integers:
        list_of_integers.append(initial_integer)
        initial_integer += increment_value
    consecutive_integers = []
    index = 0
    while (index + 3) < len(list_of_integers):
        if (list_of_integers[index] + list_of_integers[index + 1] + list_of_integers[index + 2] + list_of_integers[index + 3] == sum_of_cons_integers):
            consecutive_integers.append(list_of_integers[index])
            consecutive_integers.append(list_of_integers[index + 1])
            consecutive_integers.append(list_of_integers[index + 2])
            consecutive_integers.append(list_of_integers[index + 3])
        index += 1
    return consecutive_integers


# Check odd sequence
result = find_four_cons_integers(1, 2, sum_of_consecutive_integers)
if result:
    print(result)
else:
    # Check even sequence
    result = find_four_cons_integers(0, 2, sum_of_consecutive_integers)
    if result:
        print(result)
    else:
        # Check both sequences
        result = find_four_cons_integers(1, 1, sum_of_consecutive_integers)
        if result:
            print(result)
        else:
            print(
                "We couldn\'t find any four consecutive integers that add up to your sum.")
