"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

#Definicion de la gramatica de JavaScript
grammar = """

    ?start: exp+ 
        

    ?cualquiercosa:  /[^}]+/ -> parsefun

    ?parameters: 
        | identifier       
        | identifier "," parameters -> saveparams
       
    ?arguments:
        | atom
        | atom "," arguments -> sendarguments


    ?exp: identifier "=" expresion ";" -> assigvar
        | "console" "." "log" "(" expresion ")" ";" -> print
        | "console" "." "err" "(" expresion ")" ";" -> print
        | "function" identifier "(" parameters ")" "{" cualquiercosa "}" -> savefun
        | identifier "(" arguments ")" ";" -> exefun
        
    ?expresion: aritmeticexpresion
        | conditonexpresion
        | identifier "(" parameters ")"         

    ?conditonexpresion: expresion "==" aritmeticexpresion -> equal
        | expresion ">=" aritmeticexpresion -> greaterequal
        | expresion "<=" aritmeticexpresion -> lesserequal
        | expresion ">" aritmeticexpresion -> greater
        | expresion "<" aritmeticexpresion -> lesser

    ?aritmeticexpresion: term
        | aritmeticexpresion "+" term -> sum
        | aritmeticexpresion "-" term -> sub
    
    ?term: atom
        | term "*" atom -> mul 
        | term "/" atom -> div

    ?atom: identifier -> getvalue
        | number
        | string        

    ?identifier: /[a-zA-z]\w*/

    ?number: /\d+(\.\d+)?/

    ?string: /"[^"]*"/
        | /'[^']*'/

    %ignore /\s+/

    

"""