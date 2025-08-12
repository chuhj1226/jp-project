def solution(myString, pat):
    answer = ""
    for str1 in myString :
        if str1 == "A" :
            answer += "B"
        else :
            answer += "A"
    if answer.find(pat) == -1 :
        return 0
    return 1
