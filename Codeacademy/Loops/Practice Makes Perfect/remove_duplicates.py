def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list
