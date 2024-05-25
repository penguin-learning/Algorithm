def solution(numlist, n):
    answer = numlist
    answer.sort(key=lambda x: (abs(x-n), -x))
    return answer