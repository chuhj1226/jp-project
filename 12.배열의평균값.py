def solution(numbers):

    answer = 0
    for var in numbers :
        answer += var

    return answer / len(numbers)