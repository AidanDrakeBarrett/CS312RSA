# Project Report - RSA and Primality Tests

## Baseline

### Design Experience

The ModExp algorithm takes as input integers *x, y,* and *N*. It outputs *x^y mod N.*
It reduces the amount of time it takes to perform a modular exponent by performing a
modulo operation on each power of 2 that makes up the exponent, *y.*

| x | y | N | z | Return value |
|---|---|---|---|--------------|
| 3 | 6 | 21 | 6 | 15|
| 3 | 3 | 21 | 3 | 6 |
| 3 | 1 | 21 | 1 | 3 |
| 3 | 0 | 21 |   | 1 |

>fermat(N, k): #Test positive integer *N* *k* times for primality  
> &nbsp; a = set of *k* positive integers less than *N* - 2  
> &nbsp; for all in a:  
> &nbsp; &nbsp; if ModExp(a, N - 1, N) == 1:  
> &nbsp; &nbsp; &nbsp; return prime  
> &nbsp; &nbsp; else:  
> &nbsp; &nbsp; &nbsp; return composite  

>GenPrime(nBits): #nBits is the number is bits long the prime must be  
> &nbsp; while true:  
> &nbsp; &nbsp; num = randomBits(nBits)  
> &nbsp; &nbsp; if fermat(num) == true:  
> &nbsp; &nbsp; &nbsp; return num  
> &nbsp; &nbsp; else:  
> &nbsp; &nbsp; &nbsp; continue  

I will track my empirical data by timing how long it
takes to perform each function given inputs of various
lengths.
 

### Theoretical Analysis - Prime Number Generation

#### generate_large_prime
```py
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
```

#### Time 

generate_large_prime() references fermat(), which references mod_exp().

For mod_exp(), if we measure *n* as the bit length of *y*, we know that we will need about
*log(y) = n* layers of recursion. Within each layer, we will need to perform a multiplication
of two integers that are less than or equal to the size of *y*, giving both numbers
a size of *O(n)*. Multiplying two n-bit numbers is *O(n^2)*, and if we multiply that by
the amount of recursive calls we make, we have a total complexity of *O(n^3)*.

We can then move on to fermat(). fermat() uses random.randint(1, N - 1), which has a complexity
of *O(n)* where *n* is the range between _1_ and _N - 1_ in binary. This is because randint() generates
*O(log(range))* random bits, and then adds the result to the lower number in the range.
after this, it uses the random integer in the mod_exp() algorithm. These are done sequentially,
and therefore mod_exp()'s time complexity dominates because it is higher. If we assume the value of _k_
to be a constant-- especially since we are using it as a constant in the performance tests--
this means we have _k_ iterations of _O(n^3)_, yielding a time complexity of _O(n^3)_.

generate_large_prime() uses random.getrandbits() to generate a random number. If we tell it to generate
_n_ random bits, we have a time complexity of _O(n)_. We then perform fermat(), which is _O(n^3)_,
and then check a boolean value, which is _O(1)_, and then check the length of
the prime number we generated, which is _O(n)_. We can not tell how many attempts it will take to
successfully generate a prime number of the desired length, so our best estimation of time complexity lies
in the complexity of one iteration, which is _O(n^3)_. Therefore, the final
time complexity is **O(n^3)**.

#### Space

Returning to mod_exp needing *O(n)* layers of recursion, we can store the multiplication result
at each layer in a buffer of at most size *2n*, multiplying an n-bit number
by another is only at most *2n* in size for the result. This leads to
a level complexity of *O(n)*. Multiplying that by *n* recursions,
we have a total memory complexity of *O(n^2)*.

fermat() will clear its memory after ever iteration of its loop, so we can treat the memory used for
counting iterations as a constant. Generating a random integer between _1_ and _N - 1_
will use _O(n)_ memory because it will need to allocate _n_ bits to iterate over. mod_exp()'s
space complexity is higher, so it dominates and leaves fermat() with the same complexity of _O(n^2)_.

generate_large_prime() uses _O(n)_ space where _n_ is the bit length for the prime it needs to output.
getrandbits() will need to store its output in _n_ bits, and the condition checks are constant and then _O(logn)_
bits for comparing the bit length-- which will be counted in binary-- of the generated prime to the desired number of bits.
This means that mod_exp()'s space complexity wins again, and the overall space complexity for generating prime numbers
is **O(n^2)**.

### Empirical Data

| N    | time (ms) |
|------|-----------|
| 64   | 3.98      |
| 128  | 25.34     |
| 256  | 64.64     |
| 512  | 474.19    |
| 1024 | 9992.62   |
| 2048 | 166231.09 |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: **O(n^3)** 
- Measured constant of proportionality for theoretical order: **1.935184584e-5**
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](graph1.png)

Empirical order of growth matches theoretical order of growth

## Core

### Design Experience
Extended Euclid takes two positive integers, _a_ and _b_ where _a_ >= _b_ >= 0
and outputs values _x, y,_ and _d_ where _d_ is the greatest common divisor
of _a_ and _b_, and _ax_ + _by_ = _d_. This is used for finding the second
key in an RSA pair, where the first key is (_N, e_) where _N = pq_ and _n = (p - 1)(q - 1)._
To generate a key pair



### Theoretical Analysis - Key Pair Generation

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

## Stretch 1

### Design Experience

*Fill me in*

### Theoretical Analysis - Encrypt and Decrypt

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

#### Encryption

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

#### Decryption

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

### Comparison of Theoretical and Empirical Results

#### Encryption

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

#### Decryption

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

### Encrypting and Decrypting With A Classmate

*Fill me in*

## Stretch 2

### Design Experience

*Fill me in*

### Discussion: Probabilistic Natures of Fermat and Miller Rabin 

*Fill me in*

## Project Review

*Fill me in*

