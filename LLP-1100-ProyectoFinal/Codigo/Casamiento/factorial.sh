#!/bin/bash
:'

    # ! Método Factorial.
    # * Permite calcular la multiplicación de n*(n-1)*...*(n-k), donde n-k >=1
    # @author its_anaehm
    # @versión 0.1

'

# Función que calcula el factorial de un número.
factorial() 
{
    factorial=1
    
    counter=$num
    
    while [ $counter -gt 0 ]; do
    factorial=$(( $factorial * $counter ))
    counter=$(( $counter - 1 ))
    done
    
    echo $factorial
}

num=5
if [ $num -lt 0 ]; then
    echo "ERROR"
else
    echo "THE FACTORIAL OF $num : $( factorial $num ) "
fi