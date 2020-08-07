# **Análisis e Investigación para el Proyecto**

        IS-513 Lenguajes de Programación
        Fernando Carlos Cortes Flores  -  20171030808
        Josué Ariel Izaguirre Mejía  -  20171034157
        Gabriel Enrique Escobar Banegas  -  20181005735
        Ana Evelin Hernández Martínez  -  20171001620
---

## Índice

- [**Análisis e Investigación para el Proyecto**](#análisis-e-investigación-para-el-proyecto)
  - [Índice](#índice)
  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [***Ruby***](#ruby)
    - [***JavaScript***](#javascript)
    - [***Bash***](#bash)
      - [Comentarios](#comentarios)
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
  - [Notas](#notas)
    - [1.](#1)
    - [2.](#2)
    - [3.](#3)
  - [Anexos y Evidencias Fotográficas](#anexos-y-evidencias-fotográficas)

---

## **Elementos Conceptuales**

---

### ***Ruby***

Adjuntar los componentes correspondientes a la investigación sobre Ruby en cuanto a lo solicitado en la definición del proyecto.

---

### ***JavaScript***

Adjuntar los componentes correspondientes a la investigación sobre JavaScript en cuanto a lo solicitado en la definición del proyecto.

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

##### Nombre de identificador

Los nombres de los identificadores deben estar siempre asociados 1 en la TS, pues así son localizados por el analizador semántico y por el generador de código.

La manera en que se implementará el nombre dependerá del lenguaje de programación en que se implemente la propia TS. En los lenguajes como C y C++ se puede utilizar un campo del tipo puntero a carater (char *) y reservar la memoria dinámica necesaria en cada caso. También en lenguajes como C++, Java, C#, etc. se puede utilizar directamente el tipo String (o equivalente) de la propia biblioteca del lenguaje.

Otra solución para almacenar los nombres de las variables es colocar un descriptor de cadenas de caracteres (strings) en el campo del nombre del identificador. El descriptor contiene la posición y longitud de los subcampos del string donde se encuentra enl nombre del identificador, esta forma de acceso a los identificadores es más lenta pero puede ahorrar bastante almacenamiento.

##### Atributos de los identificadores

Los identificadores se describen por medio de los atributos que dependerán del lenguaje que se esté compilando. Algunos de estos atributos se describen en los siguientes párrafos.

###### Dirección en memoria

Los lenguajes de alto nivel tienen identificadores, sin embargo en código máquina no existen identificadores, tan solo hay las direcciones donde están colocados. Si el código objeto que genera el compilador es de muy bajo nivel se tiene que asociar en todo momento a cada identificador su dirección de comienzo. En algunos casos puede que el código objeto sea a nivel de ensamblador, en dicho caso pueden no hacer falta direcciones dado que en el ensamblador se pueden utilizar identificadores.

La TS ayuda al generador de código a generar el código objeto, sustituyendo los identificadores por sus direcciones. Las direcciones suelen ser relativas, es decir desplazamientos (offsets) desde una dirección base.

###### Tipo

El atributo tipo se almacena en la TS cuando los lenguajes a compilar tienen distintos tipos de datos definidos explícita o implícitamente.

El tipo de la variable se utiliza en las comprobaciones semánticas de las sentencias. El tipo también se usa como indicación de la cantidad de memoria que debe ser reservada en tiempo de ejecución. Por ejemplo, si el tipo es integer, suele ocupar la mitad de un float. Generalmente, el tipo de una variable se almacena en forma de código, así el tipo de float se puede codificar como F, integer como I, carácter como C, etc.

El tamaño de los tipos de datos dependerá de cada implementación del lenguaje, aunque el constructor del compilador suele aprovechar al máximo las características de máximo rendimiento de la máquina objeto.

**Ejemplo:** Elementos de una Tabla de símbolos (Falta el elemento de dirección del almacenamiento en memoria)

![Tabla de Símbolos](https://drive.google.com/uc?export=view&id=1_oLm1spENvZrc8xHqFI12sL7xfbgTLS0 "SymbolTable.png")

---

## Lluvia de Ideas

---

## Bitácora

En esta sección se detallan las metas propuestas, avances y logros que se obtuvieron a lo largo de todo el proceso de creación y ejecución del Proyecto.

### *Miercóles 29/07/2020:*

Se tuvo la primera reunión de equipo para discusión de proyecto donde también se realizó detenidamente la lectura de todos los requerimientos y objetivos del proyecto. Asímismo se realizó una lista con los objetivos principales para el funcionamiento adecuado del programa, para lo que se distribuyeron las diferentes asignaciones entre los integrantes.

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

Finalmente, se creó un repositorio en Github para tener lista la estructura de directorios para la entrega de proyecto.

## *Lunes 03/08/2020:*

Durante el fin de semana, se realizaron investigaciones por parte de cada integrante con respecto a los diferentes lenguajes de programación enlistados en los objetivos del proyecto. Posterior a la clase sincróna de Lenguajes de Programación, se sostuvo una reunión sincróna para comunicar avances en cuanto a la investigación que realizó cada integrante del equipo. También se comenzó a crear la gramática e implementar ciertos aspectos del programa. (Cortés y Grabiel escriban lo que deseen)

## *Martes 04/08/2020:*

Durante la sincróna, se siguió trabajando en los objetivos de cada integrante, se comenzó a probar la gramática y los avances de cada integrante. (Cortés y Gabriel pongan aqui de lo que se acuerden).

## *Miercoles 05/08/2020:*

Se siguió avanzado de manera individual en las tareas de cada estudiante y se creó la bitacora de avances del proyecto. Ana terminó la gramática de Bash.

## *Jueves 06/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Viernes 07/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Sábado 08/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Domingo 09/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Lunes 10/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Martes 11/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Miercoles 12/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## *Jueves 13/08/2020:*

> Aquí se detallarán las actividades realizadas durante el día en cuestión.

## Notas

### 1.
> Todas las reuniones de forma sincróna por parte de los integrantes del equipo se realizaron a través de la plataforma Discord. (Colocar referencias). Para cualquier otra forma de comunicación, se creó un grupo de WhatsApp con el objetivo de reportar avances o definir reuniones sincrónas.

### 2.
> El intervalo de tiempo durante el cual se sostenían las reuniones de trabajo variaban entre las 11A.M. - 10P.M.

### 3.
> Variaba el tiempo de conexión entre cada estudiante de acuerdo a la diferente dispocisión horaria de cada estudiante.

## Anexos y Evidencias Fotográficas

poner fotos aquí
