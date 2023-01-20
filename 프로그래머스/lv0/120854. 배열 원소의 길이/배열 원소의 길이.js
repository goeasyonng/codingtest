// function solution(strlist) {
//     var i=0;
//     while(i<strlist.length){
//         //const a = Array.from(strlist[i]); //배열로
//         //char[] arr = str.toCharstrlist();
//        // String[] arr = strlist.split("");
//         return strlist[i].length;
//         i++;
//         continue
//     }
//     }
function solution(strlist) {
    var answer = [];
    
    for (let i=0; i < strlist.length; i++) {
        const a = Array.from(strlist[i]); //배열로
        answer.push(a.length);
    }
    return answer
}