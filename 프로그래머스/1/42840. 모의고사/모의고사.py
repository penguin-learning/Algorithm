def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for idx, a in enumerate(answers):
        score[0] += 1 if a == one[idx % len(one)] else 0
        score[1] += 1 if a == two[idx % len(two)] else 0
        score[2] += 1 if a == three[idx % len(three)] else 0
        
    maxi = max(score)
    
    for i in range(len(score)):
        if maxi == score[i]:
            answer.append(i+1)
    
    return answer