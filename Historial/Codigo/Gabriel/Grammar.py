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
        | "console" "." "error" "(" expresion ")" ";" -> printerr
        | "function" identifier "(" parameters ")" "{" instructions "}" -> savefun
        | ifs     
        | "for" "(" exp conditionfor acumulatorfor ")""{" instructions "}" -> forstmt
        | "while" "(" conditionwhile ")" "{" instructions "}" -> whilestmt
        | expresion ";"
        | acumulator ";"
        | "return" expresion ";" -> returnop

    ?ifs: ifbracket 
        | "if" "(" expresion ")" "{" instructions "}" -> ifstmt
        | "if" "(" expresion ")" "{" instructions "}" "else" "{" instructions "}"  -> ifelsestmt

    ?ifbracket: "if" "(" expresion ")" instructionsoneline -> ifstmt
        | "if" "(" expresion ")" instructionsoneline "else" instructionsoneline -> ifelsestmt

    ?show: expresion
        | show "," expresion-> concat

    ?conditionwhile: identifier
        | atomwhile logicalstmt atomwhile ->  condionwhilecomp

    ?conditionfor: atom logicalstmt atom ";" -> condionforcomp
    
    ?acumulator: identifier "+" "+" -> increment
        | identifier "-" "-" -> decrement
    
    ?logicalstmt: "==" -> logicalequal
        | ">=" -> logicalmorethan
        | "<=" -> logicallessthan
        | ">" -> logicalmore
        | "<" -> logicalless
    
    ?parameters: -> none
        | identifier -> saveparam
        | identifier "," parameters -> saveparams
       
    ?arguments: -> none
        | expresion -> sendargument
        | expresion "," arguments -> sendarguments


    ?expresion: aritmeticexpresion
        | atom "." "length" "(" ")" -> length
        | conditonexpresion    

    ?acumulatorfor:  identifier "+" "+"-> incrementfor
        | identifier "-" "-" -> decrementfor

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
        | identifier "(" arguments ")"  -> exefun

    ?atomwhile: identifier
        | number
        | string        
        

    ?simplesegment: /[^\{\}]+/  -> parsefun

    ?r_segment: "{"segment"}" -> parser_segment

    ?segment: (simplesegment|r_segment)+ -> joinsegments

    ?instructions: segment -> parsefun

    ?identifier: /[a-zA-z]\w*/

    ?number: /\d+(\.\d+)?/

    ?string: /"[^"]*"/
        | /'[^']*'/

    ?instructionsoneline: /[^(\\n)^\{]+/

    %ignore /\/\/.+/
    %ignore /\/\*[\w\W]*\*\//
    %ignore /\s+/
        

"""