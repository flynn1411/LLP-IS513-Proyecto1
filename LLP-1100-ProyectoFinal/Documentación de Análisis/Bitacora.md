# **Análisis e Investigación para el Proyecto**

        UNIVERSIDAD NACIONAL AUTÓNOMA DE HONDURAS
        Facultad de Ingeniería
        Depeartamento de Ingeniería en Sistemas
        Clase: Lenguajes de Programación IS-513 
        Sección: 1100
        Catedrático: José Manuel Inestroza Murillo
        Estudiantes:    Fernando Carlos Cortes Flores  -  20171030808
                        Josué Ariel Izaguirre Mejía  -  20171034157
                        Gabriel Enrique Escobar Banegas  -  20181005735
                        Ana Evelin Hernández Martínez  -  20171001620
        II PAC 2020
        Fecha de entrea: Lunes 17 de Agosto de 2020
---

## Índice

- [**Análisis e Investigación para el Proyecto**](#análisis-e-investigación-para-el-proyecto)
  - [Índice](#índice)
  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [***Ruby***](#ruby)
      - [***Sobre Ruby***](#sobre-ruby)
      - [***Gramática***](#gramática)
        - [**Comentarios:**](#comentarios)
          - [Un comentario simple, o de una línea:](#un-comentario-simple-o-de-una-línea)
          - [Comentarios de múltiples lineas:](#comentarios-de-múltiples-lineas)
        - [**Tipos de Datos:**](#tipos-de-datos)
        - [**Operaciones**](#operaciones)
        - [Nombres de variables de Variables](#nombres-de-variables-de-variables)
        - [**Bloques de Instrucciones**](#bloques-de-instrucciones)
        - [**If, For, While, Funciones**](#if-for-while-funciones)
    - [***JavaScript***](#javascript)
    - [***Bash***](#bash)
      - [Comentarios](#comentarios-1)
      - [Generación de mensajes de salida](#generación-de-mensajes-de-salida)
      - [Asignaciones](#asignaciones)
      - [Estructuras de control de Flujo](#estructuras-de-control-de-flujo)
        - [Condicional](#condicional)
        - [Bucles](#bucles)
    - [Operadores Lógicos](#operadores-lógicos)
    - [Declaración y Ejecución de Funciones](#declaración-y-ejecución-de-funciones)
    - [***Tabla de Símbolos***](#tabla-de-símbolos)
      - [¿Qué es una tabla de símbolos?](#qué-es-una-tabla-de-símbolos)
    - [**Contenido de una TS**](#contenido-de-una-ts)
      - [Nombre de identificador](#nombre-de-identificador)
      - [Atributos de los identificadores](#atributos-de-los-identificadores)
        - [Dirección en memoria](#dirección-en-memoria)
        - [Tipo](#tipo)
  - [Lluvia de Ideas](#lluvia-de-ideas)
  - [Bitácora](#bitácora)
    - [*Miercóles 29/07/2020:*](#miercóles-29072020)
  - [*Lunes 03/08/2020:*](#lunes-03082020)
  - [*Martes 04/08/2020:*](#martes-04082020)
  - [*Miercoles 05/08/2020:*](#miercoles-05082020)
  - [*Jueves 06/08/2020:*](#jueves-06082020)
  - [*Viernes 07/08/2020:*](#viernes-07082020)
  - [*Sábado 08/08/2020:*](#sábado-08082020)
  - [*Domingo 09/08/2020:*](#domingo-09082020)
  - [*Lunes 10/08/2020:*](#lunes-10082020)
  - [*Martes 11/08/2020:*](#martes-11082020)
  - [*Miercoles 12/08/2020:*](#miercoles-12082020)
  - [*Jueves 13/08/2020:*](#jueves-13082020)
  - [*Domingo 16/08/2020:*](#domingo-16082020)
  - [Anexos y Evidencias Fotográficas](#anexos-y-evidencias-fotográficas)
  - [Notas](#notas)
  - [Referencias Bibliográficas](#referencias-bibliográficas)

---

## **Elementos Conceptuales**

---

### ***Ruby***

Investigación sobre el Lenguaje de Programación **Ruby**

#### ***Sobre Ruby***

Ruby es un lenguaje de programación orientado a objetos y multipropósito. Contiene una sintáxis más natural a la de otros lenguajes como [C/C++](https://www.cplusplus.com/) ó [JAVA](https://www.java.com/en/). Su implementación es a través de interpretación, por lo que su ejecución puede ser lenta en comparación a lenguajes compilados. Su uso se destaca en la web, donde se puede trabajar en Front-End o Back-End; no obstante, es capáz de ser utilizado en aplicaciones de escritorio utilizando librerías como GTK u OpenGL.

---

#### ***Gramática***

##### **Comentarios:**

###### Un comentario simple, o de una línea:

Estos comentarios comienzan con un símbolo de numeral (#), y terminan con un salto
de línea (\n). Lo que sea que se encuentre entre estos dos carácteres es aceptado.
E.G.

```ruby
#Este es un comentario simple en Ruby
a = 5
```

###### Comentarios de múltiples lineas:

Estos comentarios se pueden escribir en una o más lineas, Su comienzo se define con "=begin" y su final con "=end". E.G.

```ruby
=begin
Este es un comentario de multiples 
lineas.
1,2,
3
=end
factorial(6)
```

---

##### **Tipos de Datos:**

Según las especificaciones del proyecto, se aceptan:

- ###### Cadenas:

    Las cadenas pueden ser de una sola comilla o de comillas dóbles tal como en el ejemplo indicado:

    ```ruby
    #Comilla simple
    cadena1 = 'Hola "mundo" entre comillas dobles.'

    #Comillas dobles:
    cadena2 = "Hola 'mundo' entre comilla simple."
    ```

    Al definir cadenas, se tiene que pensar en sus métodos ya existentes en Ruby. Por lo que se incluyen en su gramática los siguentes:

    Método | Función/Operación
    --- | ---
     *uppcase* | convertir todas las letras a mayúscula.
     *downcase* | convertir todas las letras a minúscula.
     *length* | obtener la longitud de la cadena.
     *reverse* | revertir el orden de la cadena.
     *empty?* | verificar si la cadena se encuentra o no vacía.
     *swapcase* | convertir minúsculas a mayúsculas y viceversa.
     *split (token)* | separar el arreglo en lexemas (si no se reciben argumentos será en base a espacios).
     *chomp* | remueve \r o \n, solamente si se encuentra.
     *chop* | remueve el último carácter de la cadena.
     *strip* | remueve espacios en blanco de la cadena.
     *clear* | limpia todo contenido de la cadena.
     *to_i* | si la cadena es meramente de digítos, estos se convierten en tipo de dato númerico
     *index (substring)* | retorna la posición inicial de alguna subcadena que se encuentre en la cadena, de no ingresar la subcadena se retorna la primera posición.
     *count* | cuenta el número de veces que se encuentra una subcadena en otra.
     *gsub* | reemplaza cualquier instancia del parametro 1 con el parametro 2
     *concat* | concatenación de cadenas.
     *insert* | insertar una cadena en la posición indicada
    

    Asímismo, se debe de aceptar las cadenas con formato, las cuales contienen el simbolo de modulo (%) seguido de un arreglo que puede contener una o más expresiones.

    ```ruby
    respuesta = "La conversión de (%d , %d) a coordenadas polares es: %d,%d" % [x,y, theta(x,y), radio(x,y)]
    ```

- ###### Booleanos:

    Los booleanos en Ruby se definen entre **true** (verdadero) y **false** (falso).

    ```ruby
    falso = false

    verdadero = true
    ```

- ###### Números:

    Los números en Ruby pueden ser flotantes o enteros.

    ```ruby
    #números enteros
    entero = 4

    #números flotantes
    flotante = 9.81
    ```

- ###### Nulo:

    En Ruby, existe un tipo de dato para indicar nada. Es muy util para poder saber si se ha llegado al final de una lista enlazada por ejemplo, o si un argumento esperado existe. Este tipo de dato se reconoce al ingresar **nil**.

    ```ruby
    parametro = nil

    if parametro == nil
        puts "Parámetro esperado no encontrado."
    end
    ```

---

##### **Operaciones**

Entre las opercaciones disponibles se encuentran las:

- ###### Aritméticas:

    Operador | Operación
    --- | ---
    "+" | Sumar dos números
    "-" | Restar dos números
    "*" | Multiplicar dos números
    "/" | Dividir dos números
    "%" | Devolver el residuo de la división
    "**" | Exponencial

    ```ruby
    =begin
    La operacón resultante sería
    
    ( ( ( ( 2+3 )-8 ) * ( ( 2+3 )-8 ) ) /1) % 2
    =end

    suma = 2 + 3
    resta = suma - 8
    multiplicacion = resta * resta
    division = multiplicacion / 1
    modulo = division % 2
    ```

- ###### Booleanas:

    Operador | Significado
    --- | ---
    "==" | Ambas expresiones son iguales.
    "!=" | Ambas expresiones no son iguales.
    "<" | Menor que
    "<=" | Menor o igual que
    ">" | Mayor que
    ">=" | Mayor o igual que

    ```ruby
    verdadero = true
    
    falso = false

    expresion1 = verdadero == falso #retorna false
    expresion2 = verdadero != falso  #retorna true
    expresion3 = 3 >= 2 #true
    ```

    Asímismo existen operadores lógicos:

    Operador | Significado
    --- | ---
    "&&" | Conjunción
    "and" | Conjunción
    "\|\|" | Disyunción
    "or" | Disyunción
    "!" | Negación
    "not" | Negación

    ```ruby
    verdadero = true
    
    falso = false

    expresion1 = verdadero && falso #retorna false
    expresion2 = verdadero or falso  #retorna true
    ```


- ###### de Cadenas:

    Operación | Significado
    --- | ---
    cadena + cadena | Concatenación de cadenas.
    cadena*número | Repetir cadenas el número de veces indicado.

    ```ruby
    puts "Hola" + "mundo" #imprime "HolaMundo"

    puts "ja"*3 #imprime "jajaja"
    ```

- ###### de Asignación:

    Operador | Significado
    --- | ---
    = | Assignar valor a variable.
    += | Sumarle al valor actual de la variable.
    -= | Restarle al valor actual de la variable.
    *= | Multiplicarle al valor actual de la variable.
    /= | Dividirle al valor actual de la varible.
    %= | Realizar modulo al valor actual de la variable.
    **= | Realizar operación de exponente al valor actual de la variable.

---

##### Nombres de variables de Variables

Las variables en Ruby constan solamente entre letras, digitos y guión bajo ( _ ).

---

##### **Bloques de Instrucciones**

Los bloques de instrucciones se encuentran como sentencias de los if, else, for, while y funciones. Difieren de las instrucciones comunes al no poder crear funciones dentro de funciones o dentro de ifs (existen más casos pero dada la definición del proyecto solo esto es de importancia).

```ruby
if true 
    fib = fibonacci(3)

        if fib < 5
            puts "Es mayor."
        end
end
```

##### **If, For, While, Funciones**

- ###### If:

    Los if comienzan con la palabra reservada "if", opcionalmente seguido de un ***then***, existen bloques de instrucciones dentro del if. Al finalizar el if, se coloca la palabra reservada **end**.

    ```ruby
    if n=0 then
        return 1

    end
    ```

- ###### While:

    ```ruby
    while a>3 do
        suma += a
        a--
    end
    ```

- ###### For:

    ```ruby
    for i in  0..cadena.length do
        puts i
    end
    ```

- ###### Function:

    ```ruby
    def isLeapYear? year
        if ( ( (year%100 != 0) && (year%4 == 0) ) or ( year%400==0 ) )
            return true
        
        else
            return false
        end
    end
    ```

---

### ***JavaScript***

<sup>[[4]](###4:)</sup>.

---

### ***Bash***

Investigación sobre el Lenguaje de Programación **Bash**

#### Comentarios

---

**Comentarios de una linea:**

Los comentarios de una linea en Bash se generan colocando una almohadilla (numeral -> #) al inicio de la linea:

    #Este es el ejemplo de un comentario.

**Comentarios de múltiples lineas:**

Los comentarios de multiples lineas en Bash se generan de la siguiente manera:

    : ' 
        Esto es un comentario
        de multiples lineas
        en Bash
    '

> **NOTA:** " **#!** -> **Hashbang** indica donde está el archivo, en este caso el interprete de bash y se coloca al inicio de los programas."

#### Generación de mensajes de salida

---

**echo:**

***echo*** es la función que permite imprimir en pantalla.

***Ejemplo:*** Programa que despliegue en consola la frase "Hola Mundo."

    Programa1.sh:
        #!/bin/bash
        echo "Hola mundo."


    Despliegue en consola: 
        Hola mundo.

#### Asignaciones

---

**Variables de programación con Bash:**

En bash no se declara el tipo de variable pero puede ser un número, letra o cadena de caracteres.

> **Declaración de una variable:** nombre_variable=valor_variable

Para recuperar el valor de dicha variable sólo hay que anteponer el símbolo de dolar $ antes del nombre de la variable:

> $nombre_variable

***Ejemplo:*** En este programa se ejemplifica la forma de asignar variables, hacer el llamado a una variable y mostrar el contenido de una variable.

    Programa2.sh:
        #!/bin/bash
        #Asignación de una variable
        hola = 1
        #Llamado a una variable
        $hola
        #Mostrando el contenido de la variable en consola
        echo $hola


    Despliegue en consola:
        1

#### Estructuras de control de Flujo

---

##### Condicional

**If:**

La sintaxis básica de un condicional es la siguiente

    if [[ CONDICIÓN ]];
    then
        COMANDO 1 si se cumple la condición
    fi

También se puede especificar qué hacer si la condición no se cumple:

    if [[ CONDICIÓN ]];
    then
        COMANDO 1 si se cumple la condición
    else
        COMANDO 2 si no se cumple la condición
    fi

Incluso se pueden añadir más condiciones concatenando más if:

    if [[ CONDICIÓN 1 ]];
    then
        COMANDO 1 si se cumple la condición 1
    elif [[ CONDICIÓN 2 ]];
    then
        COMANDO 2 si se cumple la condición 2
    else
        COMANDO 3 si no se cumple la condición 2
    fi

---
    Programa3-1.sh
        #!/bin/bash
        if [ "UBUNTU" = "UBUNTU" ]; then
            echo "Son iguales"
        else
            echo "Son distinos"
        fi


    Despliegue en consola:
        Son iguales

---

    Programa3-3.sh
        #!/bin/bash
        Word1="UBUNTU"
        Word2="UBUNTU2"
        Word3="UBUNTU"
        if [ "$Word1" = "$Word2" ]; then
            echo "1 y 2 son iguales"
        elif [ "$Word1" = "$Word3" ]; then
            echo "1 y 3 son iguales"
        else
            echo "Son distinos"
        fi


    Despliegue en consola:
        1 y 3 son iguales

##### Bucles

**for:**

La sintaxis general de los bucles *for* se define de la siguiente manera:

    for VARIABLE in LISTA_VALORES;
    do
        COMANDO 1
        COMANDO 2
        ...
        COMANDO N
    done

***Ejemplo:*** Progrgramas básicos en Bash para la demostración de como use programan los bucles *for*.

    Programa4-1.sh
        #!/bin/bash
        for((i=1; i<=5; i++)):
        do
            echo $i
        done


    Despliegue en consola:
        1
        2
        3
        4
        5

---
    Programa4-2.sh
        #!/bin/bash
        Lista="1 2 3"
        for i in $Lista:
        do
            echo "Se imprime el $i"
        done


    Despliegue en consola:
        1
        2
        3

La sintaxis general de los bucles *while* es la siguiente:

    while [ VARIABLE operador lógico NÚMERO];
    do
        COMANDO 1
        COMANDO 2
        ...
        COMANDO N
    done

---

**While:**

***Ejemplo:*** Progrgramas básicos en Bash para la demostración de como use programan los bucles *while*.

    Programa5.sh
        #!/bin/bash
        Contador=0
        while [ $contador -lt 5]:
        do
            echo "Se imprime el $Contador"
            let contador = contador+1
        done


    Despliegue en consola:
        0
        1
        2
        3
        4

---

### Operadores Lógicos

---

Los Operadores lógicos para trabajar con valores alfanuméricos son:

| Operador | Evaluación |
|--- |--- |
| = | Igual a |
| != | Diferente de |
| > | Mayor que en orden ASCII |
| < | Menor que en orden ASCII |
| -n | La cadena no esta vacía |
| -z | La cadena esta vacía |

***Ejemplo:*** Programa para practicar con distintos operadores para valores alfanuméricos (cambie el operador lógico del condicional para poder contemplar los distintos resultados).

    Programa7.sh
        #!/bin/bash
        cadena1="a"
        cadena2="b"
        if [ "$cadena1" = "$cadena2" ]; then
            echo "Verdadero"
        else
            echo "Falso"
        fi


    Despliegue en consola:
        Falso

Los Operadores lógicos para trabajar con valores numéricos son:

| Operador | Evaluación |
|--- |--- |
| -lt | Mayor que |
| -le | Menor que |
| -eq | Igual |
| -ge | Menor o igual que |
| -gt | Mayor o igual que |
| -ne | Diferente |

***Ejemplo:*** Programa para practicar con distintos operadores para valores numéricos (cambie el operador lógico del condicional para poder contemplar los distintos resultados).

    Programa7.sh
        #!/bin/bash
        let numero1=1
        let numero2=2
        if [ "$numero1" -ne "$numero2" ]; then
            echo "Verdadero"
        else
            echo "Falso"
        fi


    Despliegue en consola:
        Verdadero

---

### Declaración y Ejecución de Funciones

---

Declaración de una función:

La declaración de una función en Bash se puede hacer de dos formas:

*Forma 1:*

    function <nombre de la función> () {
        #Contenido de la función
    }

*Forma 2:*

    <nombre de la función> () {
        #Contenido de la función
    }

***Ejemplo:*** Para una función que devuelve el mensaje "Hola Mundo."

    Programa8.sh
        #°/bin/bash
        #Función
        saludo () {
            echo "Hola Mundo."
        }
        #Llamado a la fucnión
        saludo


        Despliegue en consola:
            Hola Mundo.

***Ejemplo:*** Para una función con parametros."

    Programa9.1.sh
        #°/bin/bash
        #Función
        function saludo () {
            #$0
            echo $1
            echo $2
        }
        #Llamado a la fucnión con parametros, los cuales deben de estar separados por un espacio.
        saludar Hola Mundo.


        Despliegue en consola:
            Hola 
            Mundo.

>**NOTA:** Si ingresamos el parámetro ***$0*** en una fución está nos retornara el nombre del archivo con el que estamos trabajando.

---

### ***Tabla de Símbolos***

#### ¿Qué es una tabla de símbolos?

Las Tablas de Símbolos (TS) son estructuras de datos que almacenan toda la información de los identificadores del lenguaje fuente.

Las misiones principales de la TS en el proceso de traducción son:

- Colaborar con las comprobaciones semánticas.
- Facilitar ayuda a la generación de código.

La información almacenada en la TS depende directamente del tipo de elementos del

lenguaje específico a procesar y de las características de dicho lenguaje. Habitualmente los elementos del lenguaje que requieren el uso de la TS son los distintos tipos de identificadores del lenguaje (nombres de variables, de objetos, de funciones, de etiquetas, de clases, de métodos, etc.).

La información relativa a un elemento del lenguaje se almacena en los denominados atributos de dicho elemento. Estos atributos también varían de un tipo de lenguaje a otro y de un elemento a otro. Así ejemplos de atributos tales como nombre, tipo, dirección relativa en tiempo de ejecución, dimensiones de los arrays, número y tipo de los parámetros de procedimientos, funciones y métodos, tipos de acceso a los elementos de una clase (public, private, protected...), etc. se recogen y se guardan en la TS.

Los atributos se obtienen unas veces directamente del análisis del programa fuente, es decir, están en forma explícita (por ejemplo en la sección de declaraciones del programa fuente) y otras veces los atributos se obtienen de forma implícita a través del contexto en el que aparece el elemento en el programa fuente.

En el proceso de compilación se accede a la TS en unos determinados puntos que dependen inicialmente del número y la naturaleza de las pasadas del procesador de lenguaje y del propio lenguaje fuente a procesar. En los traductores y compiladores, las TS existen únicamente en tiempo de compilación, aunque en depuración (debug) pueden estar almacenadas en disco y dar información en tiempo de ejecución para identificar los símbolos que se deseen inspeccionar.

En los intérpretes contienen información en tiempo de ejecución.

> **NOTA:** ***Las palabras reservadas no están en la TS.***

### **Contenido de una TS**

Aunque su nombre parece indicar una estructuración en una tabla no es necesariamente ésta la única estructura de datos utilizada, también se emplean árboles, pilas, etc.

Lo que la estructura debe permitir es establecer un homomorfismo entre los ámbitos de utilización de los símbolos en el programa fuente y el modo en que aparecen en las sucesivas búsquedas en la tabla. Para ello debe manejar diferentes contextos de búsqueda que imiten los diferentes tipos de bloques del lenguaje fuente que se compila.

Los símbolos se guardan en la tabla con su nombre y una serie de atributos opcionales que dependerán del lenguaje y de los objetivos del procesador. Este conjunto de atributos almacenados en la TS para un símbolo determinado se define como registro
de la tabla de símbolos (symbol-table record).

Las clases de atributos que aparecen en una TS dependen de la naturaleza del lenguaje de programación para el cual está escrito el compilador. Por ejemplo, un lenguaje de programación puede no tener tipos, entonces el atributo tipo no necesita aparecer en la
tabla.

La organización de la TS variará según las limitaciones de memoria y tiempo de acceso donde se implemente el compilador.

La lista siguiente de atributos no es necesaria para todos los compiladores, sin embargo cada uno de ellos se puede utilizar en la implementación de un compilador particular.

- Nombre de identificador.
- Dirección en tiempo de ejecución a partir de la cual se almacenará el identificador si es una variable. En el caso de funciones puede ser la dirección a partir de la cual se colocará el código de la función.
- Tipo del identificador. Si es una función, es el tipo que devuelve la función.
- Número de dimensiones del array, o número de miembros de una estructura o clase, o número de parámetros si se trata de una función.
- Tamaño máximo o rango de cada una de las dimensiones de los arrays, si tienen dimensión estática.
- Tipo y forma de acceso de cada uno de los miembros de las estructuras, uniones o clases. Tipo de cada uno de los parámetros de las funciones o procedimientos.
- Valor del descriptor del fichero y tipo de los elementos del fichero en el caso de lenguajes basados en ficheros homogéneos.
- Número de la línea del texto fuente en que la variable está declarada.
- Número de la línea del texto fuente en que se hace referencia a la variable.
- Campo puntero para construir una lista encadenada que permita listar las variables en orden alfabético en las fases de depuración de código.

#### Nombre de identificador

Los nombres de los identificadores deben estar siempre asociados 1 en la TS, pues así son localizados por el analizador semántico y por el generador de código.

La manera en que se implementará el nombre dependerá del lenguaje de programación en que se implemente la propia TS. En los lenguajes como C y C++ se puede utilizar un campo del tipo puntero a carater (char *) y reservar la memoria dinámica necesaria en cada caso. También en lenguajes como C++, Java, C#, etc. se puede utilizar directamente el tipo String (o equivalente) de la propia biblioteca del lenguaje.

Otra solución para almacenar los nombres de las variables es colocar un descriptor de cadenas de caracteres (strings) en el campo del nombre del identificador. El descriptor contiene la posición y longitud de los subcampos del string donde se encuentra enl nombre del identificador, esta forma de acceso a los identificadores es más lenta pero puede ahorrar bastante almacenamiento.

#### Atributos de los identificadores

Los identificadores se describen por medio de los atributos que dependerán del lenguaje que se esté compilando. Algunos de estos atributos se describen en los siguientes párrafos.

##### Dirección en memoria

Los lenguajes de alto nivel tienen identificadores, sin embargo en código máquina no existen identificadores, tan solo hay las direcciones donde están colocados. Si el código objeto que genera el compilador es de muy bajo nivel se tiene que asociar en todo momento a cada identificador su dirección de comienzo. En algunos casos puede que el código objeto sea a nivel de ensamblador, en dicho caso pueden no hacer falta direcciones dado que en el ensamblador se pueden utilizar identificadores.

La TS ayuda al generador de código a generar el código objeto, sustituyendo los identificadores por sus direcciones. Las direcciones suelen ser relativas, es decir desplazamientos (offsets) desde una dirección base.

##### Tipo

El atributo tipo se almacena en la TS cuando los lenguajes a compilar tienen distintos tipos de datos definidos explícita o implícitamente.

El tipo de la variable se utiliza en las comprobaciones semánticas de las sentencias. El tipo también se usa como indicación de la cantidad de memoria que debe ser reservada en tiempo de ejecución. Por ejemplo, si el tipo es integer, suele ocupar la mitad de un float. Generalmente, el tipo de una variable se almacena en forma de código, así el tipo de float se puede codificar como F, integer como I, carácter como C, etc.

El tamaño de los tipos de datos dependerá de cada implementación del lenguaje, aunque el constructor del compilador suele aprovechar al máximo las características de máximo rendimiento de la máquina objeto.

**Ejemplo:** Elementos de una Tabla de símbolos (Falta el elemento de dirección del almacenamiento en memoria)

![Tabla de Símbolos](https://drive.google.com/uc?export=view&id=1_oLm1spENvZrc8xHqFI12sL7xfbgTLS0 "SymbolTable.png")

---

## Lluvia de Ideas

![Lluvia de Ideas 1](https://drive.google.com/uc?export=view&id=1vzKizdDypalaXWPaZEJtCItF237Uckdi "LLuvia de ideas.")

![Lluvia de Ideas 2](https://drive.google.com/uc?export=view&id=1ae3vuB-RPooulyu5Htirw9v4-JLEV-Pc "LLuvia de ideas.")

---

## Bitácora

En esta sección se detallan las metas propuestas, avances y logros que se obtuvieron a lo largo de todo el proceso de creación y ejecución del Proyecto.

### *Miercóles 29/07/2020:*

Se desarrollo la primera reunión del equipo <sup>[[1]](###1:)</sup> <sup>[[2]](###2:)</sup> en la cual se realizó la discusión de proyecto y se dío lectura a todos los requerimientos y objetivos del proyecto. De la misma manera se construyó una lista con los objetivos principales para el funcionamiento adecuado del programa y que también contendría la distribución de las diferentes asignaciones entre los integrantes del equipo.

Los objetivos iniciales fueron los siguientes (con fecha deseada de finalización para el viernes 07 de agosto):

- **Main**
  - Debe leer los argumentos de la consola.
  - Ejecutar JS
  - Crear tabla de símbolos JS
  - Detectar Ruby y Bash

- **Gramática**
  - JS(Fernando y Gabriel)
    - Comentarios simples o múltiples (// o /**/)
  - Bash(Ana)
  - Ruby(Josué)

- **Semántica JS:**
  - Asignación, Cadenas, booleanos, números y nulos
  - Comparaciones simples ( ==, <, >, <=, >=, !=)
  - Funciones ( 0-2 parámetros)
  - Length de cualquier objeto
  - If, While, for
  - Console.log , console.error(con su color respectivo)

Finalmente, se creó un repositorio en GitHub para tener lista la estructura de directorios según los requerimientos en la entrega de proyecto.

## *Lunes 03/08/2020:*

Durante el fin de semana, cada integrante del equipo realizó sus respectivas investigaciones con respecto a los diferentes lenguajes de programación enlistados en los objetivos del proyecto. Posterior a la clase sincróna de Lenguajes de Programación, En una reunión sincróna se detallaron los avances en cuanto a la investigación realizada. También se dio comienzo a crear las gramáticas e implementar ciertos aspectos del programa.

Las primeras tareas a realizar fueron el agregado de las librerías necesarias para la ejecución de Lark, además de añadir los programas principales como el main y reader encargados de leer el archivo y ejecutar el analizador.

Se construyeron las bases de la gramática y semántica de JavaScript. Se hizo uso de los ejemplos realizados durante las clases síncronas. Algunos elementos declarados en la gramática fueron las operaciones aritméticas, las asignaciones y las impresiones de consola.

La gramática de asignación permite la relación de un nombre de variable con un átomo. Un átomo es todo aquel elemento terminal existente en el programa. Los átomos declarados en la gramática son identificadores, cadenas o enteros. Se hace uso de la semántica para hacer un filtro entre las palabras reservadas y los identificadores. Valores como “null”, “false” y “true” serán determinados como identificadores pero durante el análisis semántico serán catalogados como palabras reservadas con un valor determinado.


## *Martes 04/08/2020:*

Durante la reunión sincrónica, <sup>[[2]](###2:)</sup> <sup>[[3]](###3:)</sup> se siguió trabajando en los objetivos de cada integrante de la misma forma comenzaron las pruebas del funcionamiento de las gramáticas y los avances de cada miembro del equipo.

Dondo inicio a la investigación para generar la gramática de una función en JavaScript; para la implementación de funciones fue necesario la creación de un subprograma. El subprograma será encargado de ejecutar las instrucciones cuando la función sea llamada. A través de la misma metodología fueron diseñados los bloques de condiciones. Para las declaraciones condicionales fue necesario crear las operaciones condicionales las cuales son encargadas de retornar un valor verdadero o falso de acuerdo a la proposición planteada. También se realizó la gramática para el reconocimiento de comentarios de una línea.

## *Miercoles 05/08/2020:*

De manera individual prosiguió cada miembro del equipo con sus respectivas asignaciones y se creó la bitácora de avances del proyecto. Durante el día se culminó el desarrollo de la gramática para el reconocimiento del lenguaje *Bash* y se inició con la construcción del *main.py* con el cual daban inicio las pruebas para corroborar el avance correcto de todos los elementos que ya habían sido programado para ese entonces.

Agregando también la gramática necesaria para la impresión de errores en JavaScript, se comenzó a construir la gramática de las declaraciones en bucle. Se usó el mismo enfoque de subprograma planteado el día anterior para la ejecución de una instrucción dada una condición que debe ser evaluada en cada iteración. La primera declaración en bucle a trabajar fue el “for”.

## *Jueves 06/08/2020:*

Dentro de la gramática de JavaScript se siguió trabajando en la gramática de la declaración for. Para esto fue necesario construir la gramática de los acumuladores. También se arreglaron algunos errores que se presentaban en los cierres de las llaves dentro de varios bloques de ejecución.

## *Viernes 07/08/2020:*

La funcionalidad de reconocimiento de lenguajes fue completada y probada con las gramáticas de los lenguajes Bash y Ruby. No obstante, aún queda cierta optimización o agregados que debían hacerse a las gramáticas a medida se fueran probando distintos casos en el programa ejemplo. Fue en este punto donde se comienza a probar todo el programa a través de un main.py (creado días atrás) en la carpeta "Casamiento" <sup>[[5]](###5:)</sup> siguiendo las especificaciones del proyecto. Al finalizar la funcionalidad de reconocimiento, se comenzó a trabajar en la tabla de símbolos.

Se realizó la gramática para los bucles “while” bajo la misma metodología de subprograma. También fue agregado el uso de los “returns” en las funciones haciendo que detuviera su ejecución y retornara un determinado valor.

## *Sábado 08/08/2020:*

De manera breve se trabajó en la generación de la tabla de símbolos. Logrando el procesamiento de cierta (no toda) la información sobre las variables durante la ejecución del programa.


## *Domingo 09/08/2020:*

Durante este día no se realizaron avances en el proyecto ya que los miembros del equipo debían cumplir con el resto de sus asignaciones en la carga académica.

## *Lunes 10/08/2020:*

La generación de la tabla de símbolos se logró completar y se agregó a la funcionalidad main.py junto con la ejecución de código JavaScript.

Se agregó la gramática de declaración condicional de una línea en JavaScript. Se realizaron pruebas para determinar la correcta ejecución de todas las reglas gramaticales presentes hasta el día. Además se añadieron funcionalidades extras como impresión con más de un color catalogado como impresión RGB el cual mejora el rendimiento del parser en un 150%.

## *Martes 11/08/2020:*

A manera tener un mejor orden del funcionamiento del programa, se creó la clase (y archivo) MainProgram.py en la carpeta "Core", en donde recibe un arreglo de argumentos y los procesa para llamar a las clases necesarias cuando se les requiera. Con esto, main.py solo le envia a MainProgram los argumentos ingresados por el usuario y deja que este los procese. Se tomó la decisión de colocarle al programa el nombre de "Rosetta", en referencia a la Piedra de Rosetta <sup>[[6]](###6:)</sup> y se generó un arte ASCII con el nombre del programa para cierta funcionalidad.

## *Miercoles 12/08/2020:*

Optimización y documentación de las clases MainProgram, JavaScript, Recognizer y TableGenerator.

## *Jueves 13/08/2020:*

Durante este día no se realizarón avances en el proyecto ya que los miembros del equipo debían cumplir con el resto de sus asignaciones en la carga académica.

## *Domingo 16/08/2020:*

Se terminó de agregar los elementos faltantes a la documentación del análisis y se realizó la grabación del video cuyo objetivo es explicar todos los componentes del proyecto.

## Anexos y Evidencias Fotográficas

***Evidencias de las Reuniones del Equipo***

![Reuniones](https://drive.google.com/uc?export=view&id=1UwG8s_fy7mV8rdGPF9cV9Aizmp1JrAQm "Reuniones del equipo.")
![Reuniones2](https://drive.google.com/uc?export=view&id=1uLlpgxmjYGQEy2t37cSaoNfbNQZQiyXI "Reuniones del equipo.")

***Pruebas a las Gramáricas***

![Pruebas a las gramáticas](https://drive.google.com/uc?export=view&id=1l3X2H_Rq0VeR_M3bXJVsHzOYnM8gm0nF "Pruebas a gramáticas.")

![Pruebas a las gramáticas2](https://drive.google.com/uc?export=view&id=1kG9M-rPF432wrZZiiaairjxeRanXR5XU "Pruebas a gramáticas2.")

![Pruebas a las gramáticas3](https://drive.google.com/uc?export=view&id=1vPZW0A4bFWDUbQZM4cskOO-8NcLuVDOC "Pruebas a gramáticas3.")

***Prueba al Reconocimiento de lenguajes***

![Prueba Reconocimiento del lenguaje](https://drive.google.com/uc?export=view&id=1CumIQZ96U_RFAQ-UTkfYFFHGPCJOzpeU "Prueba del reconocimiento de lenguajes.")

***Prueba a la Tabla de Símbolos***

![Prueba TS](https://drive.google.com/uc?export=view&id=1AVF67X5ak478kYxDI2otq0xNDNVGz042 "Pruebas a la Tabla de Símbolos.")

## Notas

 ### 1:
Todas las reuniones de forma sincrónica por parte de los integrantes del equipo se realizaron a través de la plataforma Discord. Los canales de texto y voz fueron creados para el proyecto y ocultos a la vista de cualquier tercero. Para mantener la privacidad, se le permitió el acceso unicamente a los miembros del equipo a tráves de roles únicos (con el nombre "Lingüistas"). Para cualquier otra forma de comunicación, se creó un grupo de WhatsApp con el objetivo de reportar avances o definir reuniones sincrónas.

![Permisos del rol "Lingüistas"](https://cdn.discordapp.com/attachments/739957930660593714/745005729903149196/unknown.png)

![Miembros con el rol "Lingüistas"](https://cdn.discordapp.com/attachments/739957930660593714/745010333755637760/unknown.png)

![Canal de Texto "proyecto"](https://cdn.discordapp.com/attachments/739957930660593714/745011703217127475/unknown.png)

 ### 2:
El intervalo de tiempo durante el cual se sostenían las reuniones de trabajo variaban entre las 11A.M. - 10P.M.

 ### 3:
Variaba el tiempo de conexión entre cada estudiante de acuerdo a la diferente disposición horaria de cada estudi ante.

 ### 4:
Ya que los estudiantes contaban con una noción sobre los componentes de JavaScript previo a la realización del proyecto, no se realizó una investigación tan profunda con respecto al mismo.

 ### 5:
El nombre "***Casamiento***" proviene del plato de comida típico de Honduras en el cual se mezcla el arroz y frijoles, junto con otros ingredientes, para obtener un solo platillo. Lo anterior sirve como analogía para hacer referencia a la unificación de códigos redactados por distintos integrantes del equipo.

![Casamiento](https://www.recetashonduras.com/base/stock/Recipe/178-image/178-image_web.jpg)

### 6:
La Piedra de Rosetta es una piedra encontrada por el ejercito francés en 1799. Esta piedra contiene contiene el mismo mensaje en tres distintas formas de escritura, las cuales son hierático, griego antiguo y jeroglíficos egipcios. La importancia recae en este último sistema de escritura, ya que los jeroglíficos egipcios eran un sistema muerto el cual nadie podía entender más se encontraba en todos los sitios arqueológicos en Egipto. Por ende, la Piedra Rosetta fue una pieza clave en poder interpretar el lenguaje de jeroglíficos. Fue en base a este artefacto que se le decidió poner el nombre de Rosetta al programa del proyecto, haciendo referencia a su gran valor para interpretar distintos lenguajes. Más información sobre la Piedra de Rosetta [aqui](https://www.saberespractico.com/curiosidades/que-es-la-piedra-de-rosetta/).

![Piedra de Rosetta](https://cursosnz.es/jonkcoches/wp-content/uploads/2019/04/708-2-1.jpg)

## Referencias Bibliográficas

[1]A. Aquilino, J. Cueva Lovelle, F. Ortín Soler, R. Izquierdo Castanedo, M. Luengo Díez and J. Labra Gayo, Cuadernos Didácticos - Tablas de Símbolos de Procesadores de Lenguaje (Cuaderno Nº 41), 1ra ed. Oviedo - España: SERVITEC, 2020, pp. 5-21.

[2]J. Ortiz, "Programación en Bash - parte 1", Desde Linux, 2013.

[3]D. Rodriguez, BASH Scripting. 2014, pp. 1-9.
