from math import sqrt

def solution(n):
    answer = -1
    
    for i in range(int(sqrt(n) // 1) + 1):
        if i * i == n:
            answer = 1
            break
            
    if answer == -1:
        answer = 2
    
    return answer