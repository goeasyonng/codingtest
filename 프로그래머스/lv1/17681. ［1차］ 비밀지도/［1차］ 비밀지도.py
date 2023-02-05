def solution(n, arr1, arr2):
    re=0 #다시 생성되는 몫
    to=0 #몫
    a=0 #나머지
    sum=0 #이진수의 길이
    ar1=[]
    ar2=[]
    arsum1=[]
    arsum2=[]
    #이진수 구하는 공식
    for i in range(len(arr1)):
        re=arr1[i]
        
        while(sum<n):
            if re!=0:
                to=re//2
                a=re%2
                ar1.append(a)
                sum+=1
                re=to
            else:
                ar1.append(0)
                sum+=1
        sum=0
        ar1.reverse()  
        arsum1.append("".join(map(str, ar1)))
        ar1=[]
        
    
    
    for i in range(len(arr2)):
        re=arr2[i]
        
        while(sum<n):
            if re!=0:
                to=re//2
                a=re%2
                ar2.append(a)
                sum+=1
                re=to
            else:
                ar2.append(0)
                sum+=1
        sum=0
        ar2.reverse() 
        arsum2.append("".join(map(str, ar2)))
        ar2=[]
        
    rear1=""
    rear2=""
    resumar = ""
    answer=[]
    
    for k in range(n):
        rear1=arsum1[k]
        rear2=arsum2[k]

        for p in range(n):
            if rear1[p] == "1" or rear2[p] =="1" :
                resumar+="#"
            else :
                resumar+=" "
        answer.append(resumar)
        resumar=""

    return answer
            
            
        
    
        
    
    
            