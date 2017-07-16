def distance_from_zero(number):
    numberType = type(number)
    if(numberType == int) or (numberType == float):
        return abs(number)
    else:
        return "Nope"
