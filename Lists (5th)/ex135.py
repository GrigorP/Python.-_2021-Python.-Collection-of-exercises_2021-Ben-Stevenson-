# Exercise 135. Sieve of Eratosthenes

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [i for i in range(2, n + 1) if primes[i]]
    return prime_numbers

def main():
    limit = int(input("Enter the upper limit to find prime numbers up to: "))
    primes = sieve_of_eratosthenes(limit)
    print("Prime numbers up to", limit, ":", primes)

if __name__ == "__main__":
    main()