def solution(A, B):
    answer = -1
    
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            answer = i
            break
    
    return answer