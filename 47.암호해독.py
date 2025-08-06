def solution(cipher, code):
    answer = ''
    code2 = int(code)
    for ci in cipher :        
        answer += cipher[code2-1:code2]
        code2 += int(code)
    return answer