"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

grammar = """

?start: exp+ 
    ?exp: IDENTIFIER "=" expresion ";" -> assigvar
        | "console" "." "log" "(" expresion ")" ";" -> print
        | "console" "." "error" "(" expresion ")" ";" -> printerr
        | "function" IDENTIFIER "(" parameters ")" "{" instructions "}" -> savefun
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
    ?conditionwhile: IDENTIFIER
        | atomwhile logicalstmt atomwhile ->  condionwhilecomp
    ?conditionfor: atom logicalstmt atom ";" -> condionforcomp
    
    ?acumulator: IDENTIFIER "+" "+" -> increment
        | IDENTIFIER "-" "-" -> decrement
    
    ?logicalstmt: "==" -> logicalequal
        | ">=" -> logicalmorethan
        | "<=" -> logicallessthan
        | ">" -> logicalmore
        | "<" -> logicalless
    
    ?parameters: -> none
        | IDENTIFIER -> saveparam
        | IDENTIFIER "," parameters -> saveparams

    ?arguments: -> none
        | expresion -> sendargument
        | expresion "," arguments -> sendarguments
    ?expresion: aritmeticexpresion
        | atom "." "length" "(" ")" -> length
        | conditonexpresion    
    ?acumulatorfor:  IDENTIFIER "+" "+"-> incrementfor
        | IDENTIFIER "-" "-" -> decrementfor
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
    ?atom: IDENTIFIER -> getvalue
        | NUMBER
        | STRING 
        | IDENTIFIER "(" arguments ")"  -> exefun
    ?atomwhile: IDENTIFIER
        | NUMBER
        | STRING        
        
    ?simplesegment: /[^\{\}]+/  -> parsefun
    ?r_segment: "{"segment"}" -> parser_segment
    ?segment: (simplesegment|r_segment)+ -> joinsegments
    ?instructions: segment -> parsefun
    IDENTIFIER: /[a-zA-z]\w*/
    NUMBER: /\d+(\.\d+)?/
    STRING: /"[^"]*"/
        | /'[^']*'/
    ?instructionsoneline: /[^(\\n)^\{]+/
    %ignore /\/\/.+/
    %ignore /\/\*[\w\W]*\*\//
    %ignore /\s+/
"""