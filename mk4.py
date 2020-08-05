def primes():
    """Generator which yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while True:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1


if __name__ == '__main__':
    from itertools import islice
    from datetime import datetime

    t1 = datetime.now()
    lst = list(islice(primes(), 0, 100000))
    t2 = datetime.now()
    print(f'Found {len(lst)} primes in {t2 - t1}')
