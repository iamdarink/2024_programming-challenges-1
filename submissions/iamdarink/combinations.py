from itertools import combinations_with_replacement

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_from_array(arr):
    primes = [num for num in arr if is_prime(num)]
    return primes

def primes_combinations(input_primes, target_sum):
    result = []
    for comb in combinations_with_replacement(input_primes, 2):
        if sum(comb) == target_sum:
            result.append(list(comb))    
    return result 

arr = list(map(int, input("input: ").split(",")))
input_primes = primes_from_array(arr)
target_sum = int(input("input target : "))
output = primes_combinations(input_primes, target_sum)
print("Output:", output)
