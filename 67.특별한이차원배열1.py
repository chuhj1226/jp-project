def solution(n):
    answer = []
    for x in range(n) :
        aaa = []
        for y in range(n):
            if x == y :
                aaa.append(1)
            else :
                aaa.append(0)
        answer.append(aaa)
    return answer