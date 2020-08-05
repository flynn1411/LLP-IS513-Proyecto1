"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

#Definicion de la gramatica de JavaScript
grammar = """

    ?start: exp+ 

    ?exp: identifier "=" expresion ";" -> assigvar
        | "console" "." "log" "(" expresion ")" ";" -> print
        | "console" "." "err" "(" expresion ")" ";" -> printerr
        | "function" identifier "(" parameters ")" "{" instructions "}" -> savefun
        | "if" "(" expresion ")" "{" instructions "}" -> ifstmt
        | "if" "(" expresion ")" "{" instructions "}" "else" "{" instructions "}"  -> ifelsestmt
        | "for" "(" exp conditonexpresion ";" identifier "+" "+" ")" "{" instructions"}" -> forstmt
        | expresion 

    ?parameters: 
        | identifier       
        | identifier "," parameters -> saveparams
       
    ?arguments:
        | atom
        | atom "," arguments -> sendarguments

    ?expresion: aritmeticexpresion
        | atom "." "length" "(" ")" -> length
        | identifier "(" arguments ")" ";" -> exefun
        | conditonexpresion      

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

    ?instructions:  /[^}]+/ -> parsefun

    %ignore /\/\/.+/
    %ignore /\s+/
        

    

"""