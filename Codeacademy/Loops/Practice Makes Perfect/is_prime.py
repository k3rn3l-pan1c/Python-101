def is_prime(x):
    if x <= 1:
        return False

    for num in range(2, x-1):
        if not x % num:
            return False

    else:
        return True
