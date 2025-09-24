import sys
from time import time
import random


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if (y % 2 == 0):
        return z ** 2 % N
    else:
        return x * z ** 2 % N


def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    if N % 2 == 0 and N > 2:
        return False
    for i in range(k):
        rand_num = random.randint(1, N - 1)
        modulation = mod_exp(rand_num, N - 1, N)
        if modulation != 1:
            return False
    return True


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    if N % 2 == 0 and N > 2:
        return False
    t: int = 0
    u: int = N - 1
    while True:
        u = u // 2
        t += 1
        if u % 2 == 1:
            break
    bases = []
    for i in range(k):
        bases.append(random.randint(1, N - 1))
    for i in bases:
        results = []
        for j in range(t + 1):
            results.append(mod_exp(bases[i], ((2 ** j) * u), N))
        if results[t] != 1:
            return False
        if results[0] == 1 or results[0] == N - 1:
            continue
        for j in range(1, t + 1):
            if results[j] != N - 1:
                return False
    return True


def generate_large_prime(n_bits: int) -> int:
    while True:
        prime_num = random.getrandbits(n_bits)
        primality: bool = miller_rabin(prime_num, 20)
        if primality == True:
            return prime_num
        else:
            continue
    """Generate a random prime number with the specified bit length"""
    return 4  # https://xkcd.com/221/
    #Clever^. This feels like the time for a Deus Ex reference, but I don't have any. What a shame.


def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
