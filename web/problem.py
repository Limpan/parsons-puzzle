def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
