def prime_generator(limit):
    primes = []
    for possible_prime in range(2, limit + 1):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes


print(prime_generator(100))
