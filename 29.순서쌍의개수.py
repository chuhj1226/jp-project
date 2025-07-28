def solution(n):
    li = set()
    for i in range(1,n+1):
        if n % i == 0 :
            li.add((i,n//i))
            li.add((n//i,i))

    return len(li)