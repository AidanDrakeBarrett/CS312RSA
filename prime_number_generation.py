import sys
from time import time
import random
sys.setrecursionlimit(5000)

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
    if N % 2 == 0 and N > 2:
        return False
    t: int = 1
    u: int = 0
    while True:
        u = (N - 1) // (2**t)
        if u % 2 == 1:
            break
        else:
            t += 1
            continue
    for i in range(k):
        rand_num = random.randint(1, N-1)
        if mil_rab_support(u, t, rand_num, N) == False:
            return False
    return True

def mil_rab_support(u: int, t: int, a: int, N: int) -> bool:
    a_exponent = []
    if mod_exp(a, ((2 ** t) * u), N) != 1:
        return False
    for i in range(t + 1):
        a_exponent.append(mod_exp(a, ((2 ** i) * u), N))
    if a_exponent[0] != 1:
        ind: int = 1
        while True:
            if a_exponent[ind] == 1:
                break
            else:
                ind += 1
        if a_exponent[ind - 1] % N != -1 % N:
            return False
        else:
            return True
    else:
        return True


def generate_large_prime(n_bits: int) -> int:
    while True:
        prime_num = random.getrandbits(n_bits)
        primality: bool = fermat(prime_num, 20)
        if primality == True:
            if prime_num.bit_length() == n_bits:
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
