#!/usr/bin/python3
"""
Determines the winner of the prime game.
"""


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of the prime game for given rounds and nums."""
    # Count of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Loop through each round
    for n in nums:
        # Count of primes in the range [1, n]
        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        
        # If the count is odd, Maria wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
