def reverse(string):
    reversed_str = ""
    for item in range(len(string)-1, -1, -1):
        print item
        reversed_str += string[item]

    return reversed_str
