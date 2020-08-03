"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

#Definicion de la gramatica de JavaScript
grammar = """

    ?start: exp+

    ?exp: var "=" expresion ";" -> assigvar
        | "console" "." "log" "(" expresion ")" ";" -> print
        | "console" "." "err" "(" expresion ")" ";" -> print

    ?expresion: aritmeticexpresion
        | aritmeticexpresion "==" term -> equal
        | aritmeticexpresion ">=" term -> greaterequal
        | aritmeticexpresion "<=" term -> lesserequal
        | aritmeticexpresion ">" term -> greater
        | aritmeticexpresion "<" term -> lesser

    ?aritmeticexpresion: term
        | aritmeticexpresion "+" term -> sum
        | aritmeticexpresion "-" term -> sub
    
    ?term: factor
        | term "*" factor -> mul 
        | term "/" factor -> div

    ?factor: atom

    ?atom: var -> getvar
        | number
        | string
        | bool
        | null

    ?var: /[a-zA-z]\w*/

    ?number: /\d+(\.\d+)?/

    ?string: /"[^"]*"/
        | /'[^']*'/

    ?bool: /true/
        |  /false/  

    ?null: /null/

    %ignore /\s+/


"""