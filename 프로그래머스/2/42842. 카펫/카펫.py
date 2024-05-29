def solution(brown, yellow):
    answer = []
    
    s = brown + yellow
    
    for i in range(1, s):
        if s % i == 0:
            w = max(i, s//i)
            h = min(i, s//i)
        
            if w-2 > 0 and h-2 > 0 and (w-2) * (h-2) == yellow:
                answer = [w, h]
                break
        
    return answer