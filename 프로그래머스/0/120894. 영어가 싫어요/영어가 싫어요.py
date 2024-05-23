def solution(numbers):
    answer = 0
    
    number_dict = {"zero" : '0',
                   "one" : '1',
                   "two" : '2',
                   "three" : '3',
                   "four" : '4',
                   "five" : '5',
                   "six" : '6',
                   "seven" : '7',
                   "eight" : '8',
                   "nine" : '9'}
    
    for num in number_dict:
        numbers = numbers.replace(num, number_dict[num])
    
    answer = int(numbers)
    
    return answer