from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set([])
    
    primes = [True for i in range(int(1e7)+1)]
    primes[0] = False
    primes[1] = False
    
    for i in range(2, int(1e7 ** 0.5)+1):
        if primes[i] == False:
            continue
        else:
            j = 2
            while i * j <= 1e7:
                primes[i*j] = False
                j += 1
    
    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            p = int(''.join(p))

            if p not in nums:
                nums.add(p)
            else:
                continue

            if primes[p] == True:
                answer += 1      
    
    return answer