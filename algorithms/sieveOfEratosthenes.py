# print prime numbers from 2 to limit(n) using sieve of eratosthenes algorithm

def sieveOfEratosthenes(n: int) -> list[int]:
    prime = list(range(n + 1))

    prime[1] = 0

    for i in range(2, n + 1):
        if prime[i] != 1:
            for j in range(i * i, n + 1, i):
                prime[j] = 0

    filteredPrime = []

    for i in prime:
        if i != 0:
            filteredPrime.append(i)

    print(filteredPrime)

sieveOfEratosthenes(50)
