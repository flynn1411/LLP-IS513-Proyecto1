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
	este = "variable interna";
	if (n < 2){
		return 1;
	}

	return n*factorial(n-1);
}

function imprimirFactorial(n, fact){
	message = "El factorial de ";
	message2 = " es: ";

	console.log(message, n ,message2, fact);
}

imprimirFactorial(b, factorial(b));