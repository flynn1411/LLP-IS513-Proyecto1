function factorial(n){
    if (n == 1) {return 1;}
    if(n==0) {return 1;}

    return n*factorial(n-1);
}
/*Esta onda aguanta hasta 44 */
for(i=0;i<5;i++){
    console.error("El factorial de",i,":",factorial(i));    
}