function factorial(n){
    if (n==1){
        if(true){
            return 1;  
        }
    } 
    if (n<1){
        return 1;  
    } 
    return n*factorial(n-1);
}

   
n=5;
console.log(factorial(n));