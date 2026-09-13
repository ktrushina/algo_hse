from prime import count_primes

def test_1():
    assert count_primes(1) == 0

def test_2():
    assert count_primes(2) == 0

def test_3():
    assert count_primes(3) == 1

def test_20():
    assert count_primes(20) == 8



