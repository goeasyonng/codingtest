def solution(s):
# 반복문으로 현재 요소와 다음요소가 같은지 확인한다.
# 같으면 a+1, 다르면 b+1을 한다
# a와 b가 같아지는 순간 빈문자열에 넣는다.
# 다음 문자자부터 앞의 과정을 반복한다.
# 마지막은 그냥 배열에 넣는다.
    a=0 #문자 같을 때
    b=0 #문자 다를 때
    sum=0
    tmp = ""
    for i in range(0,len(s)):
        if not tmp:
            tmp = s[i]
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