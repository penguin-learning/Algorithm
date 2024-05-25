def solution(before, after):
    answer = 1
    
    num_before = {}
    num_after = {}
    
    for b in list(before):
        if b not in num_before:
            num_before[b] = 1
        else:
            num_before[b] += 1
    
    for a in list(after):
        if a not in num_after:
            num_after[a] = 1
        else:
            num_after[a] += 1
    
    for k in num_after:
        if k not in num_before or num_after[k] != num_before[k]:
            answer = 0
            break
            
    return answer