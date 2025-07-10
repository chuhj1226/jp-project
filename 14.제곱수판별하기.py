import math
def solution(n):
    answer = 0
    if math.isqrt(n) ** 2 == n :
        answer = 1
    else :
        answer = 2
    return answer