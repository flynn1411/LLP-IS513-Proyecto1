a = "Hola";
b = " Mundo";
a = 1;
suma = a + 1;





for(i=0;i<3;i++){
	console.error("Bienvenido a ROSETTA");
}

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

imprimirFactorial(5, factorial(5));