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
        | "for" "(" exp conditionfor increment ")""{" instructions "}" -> forstmt
        | expresion 
        
    
    ?simplesegment: /[^\{\}]+/  -> parsefun
    ?r_segment: "{"segment"}" -> parser_segment
    ?segment: (simplesegment|r_segment)+ -> joinsegments
    ?instructions: segment -> parsefun

    ?conditionfor: atom logicalstmt atom ";" -> condionforcomp
    
    ?logicalstmt: "==" -> logicalequal
        | ">=" -> logicalmorethan
        | "<=" -> logicallessthan
        | ">" -> logicalmore
        | "<" -> logicalless
    
    ?parameters: -> none
        | identifier -> saveparam
        | identifier "," parameters -> saveparams
       
    ?arguments: -> none
        | atom -> sendargument
        | atom "," arguments -> sendarguments

    ?expresion: aritmeticexpresion
        | atom "." "length" "(" ")" -> length
        | identifier "(" arguments ")" ";" -> exefun
        | conditonexpresion    

    ?increment:  identifier "+" "+"-> incremento
        | identifier "-" "-" -> decrement

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


    %ignore /\/\/.+/
    %ignore /\/\*[\w\W]*\*\//
    %ignore /\s+/
        

"""