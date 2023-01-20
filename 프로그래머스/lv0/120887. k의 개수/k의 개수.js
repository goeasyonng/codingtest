function solution(i, j, k) {
    var z=0;
    for(i; i<=j; i++){
        const str = String(i); //문자열로
        const a = Array.from(str); //배열로
        for(var l=0; l<=a.length; l++){
            if(a[l]==k){
                z++;
            }
            else{
                
            }
        }
    }
    return z;
}