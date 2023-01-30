def solution(s):
    a=0 #문자 같을 때
    b=0 #문자 다를 때
    sum=0
    tmp = ""
    for i in range(0,len(s)):
        if not tmp:
            tmp = s[i]
            #기준문자로 tmp가 비워져있지 않다면 tmp값은 유지된다. 따라서 a와 b가 같아지는 순간만 문자열이 비어진채 초기화 되므로 tmp값이 그때 바뀌게 된다.
        if tmp == s[i]:
            a+=1
        else:
            b+=1
            
        if a==b:
            sum+=1
            a,b = 0,0
            tmp =""
    if tmp:
        sum+=1
    return sum
