def solution(sides):
    answer = 1
    long = max(sides)
    sides.remove(long)
    total = sum(sides)
    if long >= total :
        answer = 2
    
    return answer