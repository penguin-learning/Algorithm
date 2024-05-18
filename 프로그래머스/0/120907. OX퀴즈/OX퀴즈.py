def solution(quiz):
    answer = []
    
    for q in quiz:
        eq, ans = q.split("=")

        if eval(eq) == int(ans):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer