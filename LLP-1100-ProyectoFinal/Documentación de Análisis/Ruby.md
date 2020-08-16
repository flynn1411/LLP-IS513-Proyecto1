# Investigación sobre Ruby

---

## ***Sobre Ruby***

Ruby es un lenguaje de programación orientado a objetos y multiprpósito. Contiene una sintáxis más natural 
a la de otros lenguajes como [C/C++](https://www.cplusplus.com/) ó [JAVA](https://www.java.com/en/). Su implementación es a través de interpretación, por lo que 
su ejecución puede ser lenta en comparación a lenguajes compilados. Su uso se destaca en la web, donde se puede trabajar en Front-End o Back-End; no obstante, es capáz de ser utilizado en aplicaciones de escritorio utilizando librerías como GTK u OpenGL.

---

## ***Gramática***

### **Comentarios:**

#### Un comentario simple, o de una línea:

Estos comentarios comienzan con un símbolo de numeral (#), y terminan con un salto
de línea (\n). Lo que sea que se encuentre entre estos dos carácteres es aceptado.
E.G.

```ruby
#Este es un comentario simple en Ruby
a = 5
```

#### Comentarios de múltiples lineas:

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

### **Tipos de Datos:**

Según las especificaciones del proyecto, se aceptan:

- ##### Cadenas:

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

- #### Booleanos:

    Los booleanos en Ruby se definen entre **true** (verdadero) y **false** (falso).

    ```ruby
    falso = false

    verdadero = true
    ```

- #### Números:

    Los números en Ruby pueden ser flotantes o enteros.

    ```ruby
    #números enteros
    entero = 4

    #números flotantes
    flotante = 9.81
    ```

- #### Nulo:

    En Ruby, existe un tipo de dato para indicar nada. Es muy util para poder saber si se ha llegado al final de una lista enlazada por ejemplo, o si un argumento esperado existe. Este tipo de dato se reconoce al ingresar **nil**.

    ```ruby
    parametro = nil

    if parametro == nil
        puts "Parámetro esperado no encontrado."
    end
    ```

---

### **Operaciones**

Entre las opercaciones disponibles se encuentran las:

- #### Aritméticas:

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

- #### Booleanas:

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


- #### de Cadenas:

    Operación | Significado
    --- | ---
    cadena + cadena | Concatenación de cadenas.
    cadena*número | Repetir cadenas el número de veces indicado.

    ```ruby
    puts "Hola" + "mundo" #imprime "HolaMundo"

    puts "ja"*3 #imprime "jajaja"
    ```

- #### de Asignación:

    Operador | Significado
    --- | ---
    = | Assignar valor a variable.
    += | Sumarle al valor actual de la variable.
    -= | Restarle al valor actual de la variable.
    *= | Multiplicarle al valor actual de la variable.
    /= | Dividirle al valor actual de la varible.
    %= | Realizar modulo al valor actual de la variable.
    ** | Realizar operación de exponente al valor actual de la variable.

---

### Nombres de variables de Variables

Las variables en Ruby constan solamente entre letras, digitos y guión bajo ( _ ).

---

### **Bloques de Instrucciones**

Los bloques de instrucciones se encuentran como sentencias de los if, else, for, while y funciones. Difieren de las instrucciones comunes al no poder crear funciones dentro de funciones o dentro de ifs (existen más casos pero dada la definición del proyecto solo esto es de importancia).

```ruby
if true 
    fib = fibonacci(3)

        if fib < 5
            puts "Es mayor."
        end
end
```

### **If, For, While, Funciones**

- #### If:

    Los if comienzan con la palabra reservada "if", opcionalmente seguido de un ***then***, existen bloques de instrucciones dentro del if. Al finalizar el if, se coloca la palabra reservada **end**.

    ```ruby
    if n=0 then
        return 1

    end
    ```

- #### While:

    ```ruby
    while a>3 do
        suma += a
        a--
    end
    ```

- #### For:

    ```ruby
    for i in  0..cadena.length do
        puts i
    end
    ```

- #### Function:

    ```ruby
    def isLeapYear? year
        if ( ( (year%100 != 0) && (year%4 == 0) ) or ( year%400==0 ) )
            return true
        
        else
            return false
        end
    end
    ```

