function solution(order) {
    var k=0;
    const str = String(order); //문자열로
    const a = Array.from(str); //배열로
    for(var i=0; i<=a.length; i++){
        if(a[i] ==3){
            k++;
        }
        else if(a[i] ==6){
            k++;
        }
        else if(a[i] ==9){
            k++;
        }
        else{
            
        }
    }
    return k;
}