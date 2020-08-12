hola = "Mundo";

numero = 2.43;

a = 4;

b = 5;

cadena = "Esta es una cadena";

numero = "ahora es una cadena";

cadena = a;

cadena = a + b;

booleano = true;

hola = "3";
console.log(cadena);

function factorial(n){
    if(n<2){
        return 1;
    }
    return n*factorial(n-1);
}

while(booleano){
    a = 5;
    booleano = false;
}

fact = factorial(5);

console.log(fact);
//No tiene punto y coma, por lo que fallará
var2 = 5;