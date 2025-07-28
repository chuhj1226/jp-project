def solution(my_string):
    answer = []
    for str in my_string :
        answer.extend(str)
        
    answer.reverse()
    answer = ''.join(answer)
    return answer 