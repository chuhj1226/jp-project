def solution(hp):
    answer = 0 
    
    for h in range(hp) :
       
        if hp >= 5 :
            hp -= 5
            answer += 1
        elif hp >= 3 :
            hp -= 3
            answer += 1
        elif hp >= 1 :
            hp -= 1
            answer += 1
        
    
    return answer