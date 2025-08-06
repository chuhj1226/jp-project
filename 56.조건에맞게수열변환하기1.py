def solution(arr):
    answer = []
    for ar in arr :
        if ar >= 50 and ar % 2 == 0 :
            answer.append(ar/2)
        elif ar < 50 and ar % 2 != 0 :
            answer.append(ar*2)
        else :
            answer.append(ar)
    return answer