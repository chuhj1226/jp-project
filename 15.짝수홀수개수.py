def solution(num_list):
    answer = []
    var = 0
    var2 = 0
    for num in num_list :
        if num % 2 == 1 :
            var2 += 1
        elif num % 2 == 0 :
            var += 1
            
    answer.extend([var,var2])
    return answer