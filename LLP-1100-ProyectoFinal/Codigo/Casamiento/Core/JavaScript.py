# -*- coding: utf-8 -*-

from Core.Semantic import Semantic
from Core.lark import Lark, Tree, Token, Transformer, UnexpectedInput
from Core.Grammars.javaScript import *

"""
? Clase que maneja la ejecución de código JavaScript
! 
"""
class JavaScript:
    def __init__(self): pass

    def runCode(self, fileContents):
        semantic = Semantic(mode = True)

        parser = Lark(grammar, parser="lalr", transformer=semantic)

        try:
            parser.parse("%s\n"%fileContents)

        except UnexpectedInput as unexpectedInput:
            quit(
                "Se ha detectado un error de sintáxis en la línea %s, columna %s.\n\nLínea del error:\n\n%s"
                %(
                    unexpectedInput.line,
                    unexpectedInput.column, 
                    unexpectedInput.get_context(fileContents)
                    )
                )