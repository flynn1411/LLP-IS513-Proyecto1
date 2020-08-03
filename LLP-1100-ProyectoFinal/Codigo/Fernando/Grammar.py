"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

#Definicion de la gramatica de JavaScript
grammar = """

    //
    strat: exp?

    exp: var "=" expresion -> assigvar

    expresion: aritmeticexpresion


    aritmeticexpresion: atom
        | aritmeticexpresion "+" atom -> sum
        

    atom: var -> getvar
        | number
        | string
        | bool
        | null

    var: /[a-zA-z]\w*/

    number: /\d+(\.\d+)?/

    string: /"[^"]*"/
        | /'[^']*'/

    bool: /true/
        |  /false/  

    null: /null/







"""