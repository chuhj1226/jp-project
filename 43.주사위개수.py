def solution(box, n):
    garo = box[0] // n
    sero = box[1] // n
    high = box[2] // n
    answer = garo*sero*high
    return answer