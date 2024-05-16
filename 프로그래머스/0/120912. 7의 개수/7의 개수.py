def solution(array):
    answer = 0
    
    for a in array:
        for c in str(a):
            if c == '7':
                answer += 1
    
    return answer