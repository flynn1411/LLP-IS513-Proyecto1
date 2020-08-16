# -*- coding: utf-8 -*-

from Core.Semantic import Semantic
from Core.lark import Lark, Tree, Token, Transformer, UnexpectedInput
from Core.Grammars.javaScript import *

"""
! Clase que maneja la ejecución de código JavaScript
? Contiene un único método que ejecuta los contenidos de un archivo con código JavaScript.
@author: flynn1411
@version: 0.2
@date: 11/08/2020
"""
class JavaScript:
    def __init__(self, rgb = False):
        self.rgb = rgb

    """
    ! Método encargado de ejecutar código
    ? Obtiene los contenidos de un archivo y realiza el parseo  y ejecución utilizando Lark.
    ? De tener un error, se le informa al usuario mediatne un mensaje que incluye la fila y columna del error.
    @param fileContents Los contenidos del archivo ingresado por el usuario como parámetro del usuario.
    """
    def runCode(self, fileContents):
        semantic = Semantic(self.rgb)

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