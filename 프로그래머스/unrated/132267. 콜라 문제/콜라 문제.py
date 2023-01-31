def solution(a, b, n):
    i=0
    j=0
    p=n
    sum=0
    while(True):
        i=(p//a)*b
        j=p%a
        sum+=i
        if i+j <a:
            break
        else:
            p=i+j
            continue
        
    return sum