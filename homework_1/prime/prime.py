def count_primes(n):
    count = 0

    for number in range(2, n):
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count
