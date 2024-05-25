def solution(array, n):
    answer = [[x, abs(x-n)] for x in array]
    answer.sort(key=lambda x: (x[1], x[0]))
    answer = answer[0][0]
    return answer