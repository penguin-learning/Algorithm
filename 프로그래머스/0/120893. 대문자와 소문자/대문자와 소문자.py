def solution(my_string):
    answer = ''
    
    for s in my_string:
        if 'a' <= s and s <= 'z':
            answer += chr(ord('A') + (ord(s) - ord('a')))
        elif 'A' <= s and s <= 'Z':
            answer += chr(ord('a') + (ord(s) - ord('A')))
    
    return answer