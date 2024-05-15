def solution(M, N):
    answer = max(M,N) * (min(M,N) - 1) + max(M,N) - 1
    return answer