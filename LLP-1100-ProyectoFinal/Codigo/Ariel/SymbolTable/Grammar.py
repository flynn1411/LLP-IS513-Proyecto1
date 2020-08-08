"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

#Definicion de la gramatica de JavaScript
grammar = """

    start: exp+ 

    exp: IDENTIFIER "=" expresion ";" -> assignvalue
        | "console" "." "log" "(" expresion ")" ";"
        | "console" "." "err" "(" expresion ")" ";"
        | "function" IDENTIFIER "(" parameters ")" "{" instructions "}"
        | "if" "(" expresion ")" "{" instructions "}"
        | "if" "(" expresion ")" "{" instructions "}" "else" "{" instructions "}" 
        | "for" "(" exp conditionfor increment ")""{" instructions "}"
        | expresion 
        
    
    simplesegment: /[^\{\}]+/ 

    r_segment: "{"segment"}"

    segment: (simplesegment|r_segment)+

    instructions: segment

    conditionfor: atom logicalstmt atom ";"
    
    logicalstmt: "=="
        | ">="
        | "<="
        | ">"
        | "<"
    
    parameters:
        | IDENTIFIER
        | IDENTIFIER "," parameters

    arguments:
        | atom
        | atom "," arguments

    expresion: aritmeticexpresion
        | atom "." "length" "(" ")"
        | IDENTIFIER "(" arguments ")" ";"
        | conditonexpresion    

    increment:  IDENTIFIER "+" "+"
        | IDENTIFIER "-" "-"

    conditonexpresion: expresion "==" aritmeticexpresion
        | expresion ">=" aritmeticexpresion
        | expresion "<=" aritmeticexpresion
        | expresion ">" aritmeticexpresion
        | expresion "<" aritmeticexpresion
        

    aritmeticexpresion: term
        | aritmeticexpresion "+" term
        | aritmeticexpresion "-" term

    term: atom
        | term "*" atom
        | term "/" atom

    atom: IDENTIFIER -> getvalue
        | NUMBER
        | STRING        

    IDENTIFIER: /[a-zA-z]\w*/

    NUMBER: /\d+(\.\d+)?/

    STRING: /"[^"]*"/
        | /'[^']*'/


    %ignore /\/\/.+/
    %ignore /\/\*[\w\W]*\*\//
    %ignore /\s+/
        

"""