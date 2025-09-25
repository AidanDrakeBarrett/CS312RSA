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
lengths. I can track memory usage this way, too.
 

### Theoretical Analysis - Prime Number Generation

#### Time 

If we measure *n* as the bit length of *y*, we know that we will need about
*log(y) = n* layers of recursion. Within each layer, we will need to perform a multiplication
of two integers that are less than or equal to the size of *y*, giving both numbers
a size of *O(n)*. Multiplying two n-bit numbers is *O(n^2)*, and if we multiply that by
the amount of recursive calls we make, we have a total complexity of *O(n^3)*.

#### Space

Continuing with needing *O(n)* layers of recursion, we can store the multiplication result
at each layer in a buffer of at most size *2n*, multiplying an n-bit number
by another is only at most *2n* in size for the result. This leads to
a level complexity of *O(n)*. Multiplying that by *n* recursions,
we have a total memory complexity of *O(n^2)*.

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

