def purify(numbers):
    even_list = []
    for number in numbers:
        if not number % 2:
            even_list.append(number)

    return even_list
