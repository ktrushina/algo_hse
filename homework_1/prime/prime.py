#from math import isqrt

def count_primes(n):
    count = 0

    for number in range(2, n):
        is_prime = True

        for divisor in range(2, number): #лучше заменить на in range(2, isqrt(number)+1): O(N^2) -> O(N sqrt(N))
            #проверяем  до корня из number тк если число составное, у него обязательно есть делитель, 
            #который не больше квадратного корня из этого числа
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count
