import sys
from time import time

import prime_number_generation as prime

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]


def generate_key_pairs(n_bits) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Randomly creates a p and q (two large n-bit primes)
    Computes N = p*q
    Computes e and d such that e*d = 1 mod (p-1)(q-1)
    Return N, e, and d
    """
    p = prime.generate_large_prime(n_bits)
    q: int
    while True:
        q = prime.generate_large_prime(n_bits)
        if q == p:
            continue
        else:
            break
    N = p * q
    p_and_q = (p - 1) * (q - 1)
    for i in primes:
        x, y, d = ext_euclid(p_and_q, primes[i])
        if d == 1:
            return N, primes[i], y
    raise Exception("None of the provided primes worked with p and q.")

def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    x, y, d = ext_euclid_recursion(a, b)
    if y < 0:
        y += a
        return x, y, d
    else:
        return x, y, d

def ext_euclid_recursion(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return 1, 0, a
    x, y, d = ext_euclid(b, (a % b))
    return y, (x - (a // b) * y), d



def main(n_bits: int, filename_stem: str):
    start = time()
    N, e, d = generate_key_pairs(n_bits)
    print(f'{time() - start} seconds elapsed')

    public_file = filename_stem + '.public.txt'
    with open(public_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(e)
        ])
    print(public_file, 'written')

    private_file = filename_stem + '.private.txt'
    with open(private_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(d)
        ])
    print(private_file, 'written')


if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
