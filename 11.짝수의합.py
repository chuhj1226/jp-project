def solution(n):
    answer = 0

    for var in range(n+1) :
        if var % 2 == 0:
            answer += var

    return answer