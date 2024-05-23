def solution(order):
    answer = 0
    for s in str(order):
        if s in ['3', '6', '9']:
            answer += 1
    return answer