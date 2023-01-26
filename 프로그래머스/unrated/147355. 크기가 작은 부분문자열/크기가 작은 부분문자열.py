def solution(t, p):
    a=0
    arr=[]
    sum=0
    
    for i in range(len(t)-len(p)+1):
        arr.append(t[i:i+len(p)])
        if int(arr[i])<=int(p):
            sum+=1
        else:
            continue
        
    return(sum)
        