# -*- coding: utf-8 -*-

"""
    ! Gramática para el lenguaje de programación Bash
    * Esta gramática permite el reconocimiento de instrucciones
    ? Reconocimiento de comentarios simples y de múltiples lineas.
    ? Reconocimento de Asignaciones.
    ? Reconocimineto de declaración y ejecución de funciones.
    ? Reconocimiento de estructuras para el control de flujo.
    ? Reconocimiento de generación de mensajes de salida.
    @author its_anaehm
    @date 04/08/2020
    @version 0.1
"""

grammar = """
    //Axioma inicial
    ?start: exp+

    //Comentarios
    ?comments: "#" stringcomments
        | ":'" stringcomments+  "'"

    // Expresiones
    ?exp: "#!/bin/bash"
        | comments
        | "echo" string "$"var
        | "echo" string
        | "echo" "$"var
        | var "=" string
        | var "=" "$"? var
        | "let"? var "=" aritmeticoperation
        | var "=" "$"? boolean
        | var "=" boolean
        | var "=" nulo
        | flowcontrol
        | functions

    ?functions: "function" var"()" "{" sentence "}"
        | var"()" "{" sentence "}"

    ?flowcontrol: "if" "[" condition "];" "then" sentence "fi"
        | "else" sentence
        | "elif" sentence
        | "for""((" var "=" number ";" var logicoperator number ";" var accumulator "))" "do" sentence "done"
        | "for" var "in" "$"var ":" "do" sentence "done"
        | "while" "[" condition "];" "do" sentence "done"
        | "until" "[" condition "];" "do" sentence "done"

    ?sentence: exp
        | var "=" "$" "((" functionsentences "))"
        | comments sentence
        | "echo" string "$"var sentence
        | "echo" string sentence
        | "echo" "$"var sentence
        | var "=" "$" "((" functionsentences "))" sentence
        | var "=" string sentence
        | "let"? var "=" aritmeticoperation sentence
        | var "=""$"? boolean sentence
        | var "=" nulo sentence
        | var "=" "$"var sentence
        | flowcontrol sentence
    
    ?condition: "$"var logicoperator comparisonvariable


    ?functionsentences: atomfunctionsentences
        | functionsentences "+" atomfunctionsentences
        | functionsentences "-" atomfunctionsentences

    ?atomfunctionsentences: "$" var
        | "$"? number
        | atomfunctionsentences "*" "$"var

    ?logicoperator: numericlogicoperator
        | alfanumericlogicoperator

    ?numericlogicoperator: "=="
        | "-lt"
        | "-le"
        | "-eq"
        | "-ge"
        | "-gt"
        | "-ne"
        | ">="
        | "<="

    ?alfanumericlogicoperator: "="
        | "!="
        | ">"
        | "<"
        | "-n"
        | "-z"

    ?comparisonvariable: number
        | string
        | var

    //Definición de una operacion aritmética
    ?aritmeticoperation: atom
        | aritmeticoperation "+" atom
        | aritmeticoperation "-" atom

    //Definición de un atomo
    ?atom: number
        | atom "*" number
        | atom "/" number
        | "(" group ")"

    ?group: aritmeticoperation
    
    //Definición de una cadena en comentarios
    ?stringcomments: /.+/

    //Definición de una cadena
    ?string: /"[^"]*"/

    //Definición de una variable
    ?var: /[a-zA-Z]\w*/

    //Definición de un acumulador para trabajar en los bucles
    ?accumulator: "++"
        | "--"

    //Definición de un número
    ?number: /\d+(\.\d+)?/

    //Definición de un booleano
    ?boolean: "true"
        | "false"

    //Definición de un elemento nulo
    ?nulo: "null"

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/

"""
