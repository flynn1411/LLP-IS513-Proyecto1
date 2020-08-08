# -*- coding: UTF-8 -*-



#Definicion de la gramatica de JavaScript
grammar = """
    //Axíoma Inicial
    ?start: exp+ 

    //Definición de una Expresión
    ?exp: var "=" expression ";" 
        | "console" "." "log" "(" expression ")" ";"
        | "console" "." "err" "(" expression ")" ";"
        | expression ";"
        | acumulator ";"
        | "return" expression ";"
        | flowcontrol
        | function

    //Definición de una estructura de contol de flujo
    ?flowcontrol: "if" "(" expression ")" "{" sentence "}"
        | "if" "(" expression ")" "{" sentence "}" "else" "{" sentence "}"
        | "for" "(" exp conditionfor acumulator ")""{" sentence "}"
        | "while" "(" conditionwhile ")" "{" sentence "}"

    //Definición de una función
    ?function: "function" var "(" parameters ")" "{" sentence "}"

    ?conditionwhile: var
        | atomwhile logicalstmt atomwhile

    ?conditionfor: atom logicalstmt atom ";"

    //Definición de un acumulador
    ?acumulator: var "++"
        | var "--"
    
    //Definición de un operador lógico
    ?logicalstmt: "==" 
        | ">="
        | "<="
        | ">"
        | "<"
    
    //Definición de un parámetro
    ?parameters: none
        | var
        | var "," parameters

    //Definición de un argumento
    ?arguments: none
        | expression
        | expression "," arguments

    //Definición de una expresión
    ?expression: aritmeticexpression
        | atom ".length" "(" ")"
        | conditonexpression    

    //Definición de condicionales
    ?conditonexpression: expression "==" aritmeticexpression
        | expression ">=" aritmeticexpression
        | expression "<=" aritmeticexpression
        | expression ">" aritmeticexpression
        | expression "<" aritmeticexpression

    //Definición de una expresión aritmética
    ?aritmeticexpression: term
        | aritmeticexpression "+" term
        | aritmeticexpression "-" term

    //Definición de un término
    ?term: atom
        | term "*" atom
        | term "/" atom

    //Definición de un atomo
    ?atom: var
        | number
        | string 
        | var "(" arguments ")"

    //Definivión de un atomo para la estructura while
    ?atomwhile: var
        | number
        | string        
    
    //Definición de una sentencia
    ?sentence: exp
        |var "=" expression ";" sentence
        | "console" "." "log" "(" expression ")" ";" sentence
        | "console" "." "err" "(" expression ")" ";" sentence
        | expression ";" sentence
        | acumulator ";" sentence
        | "return" expression ";" sentence
        | flowcontrol sentence
        | function sentence

    //Definición de una variable
    ?var: /[a-zA-z]\w*/

    //Definición de un número
    ?number: /\d+(\.\d+)?/

    //Definición de un string
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de un none
    ?none: "none"

    %ignore /\/\/.+/
    %ignore /\/\*[\w\W]*\*\//
    %ignore /\s+/

"""