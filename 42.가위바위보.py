def solution(rsp):
    answer = rsp.translate(str.maketrans("205","052"))
    return answer