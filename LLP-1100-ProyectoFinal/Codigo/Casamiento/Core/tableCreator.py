# -*- coding: utf-8 -*-

import re
from Core.lark import Lark, Tree, Token, Transformer, UnexpectedInput
from Core.Semantic import Semantic
from Core.Grammars.javaScript import *
from tabulate import tabulate


"""
? TableCreator
! Clase encargada de generar la tabla de símbolos.
! Utiliza la misma semántica y gramática para ejecutar código de JavaScript en una de las
! funcionalidades del programa. Crea una instancia de Semantic, pero en una "modalidad" diferente
! para evitar la ejecución del programa (como los llamados a impresión de pantalla).
! Se llama al diccionario que se maneja internamente en Semantic para poder obtener los datos del Arbol de parseo.
! El resultado de todo se muestra en un arreglo utilizando tabulate.
@author: flynn1411
@version: 0.1
@date: 10/08/2020
"""
class TableCreator:
    def __init__(self):
        self.fileContents = ""
        self.header = [
            ["Intérprete de Lenguajes ILANG"],
            ["@authors: Ana Hernández, Fernando Córtes, Gabriel Escobar, Josué Izaguirre (Dream Team)"],
            ["@version: 0.1.0"],
            ["@fecha: 16/08/2020"]
            ]
        self.symbolTable = []
        self.parseTree = None
        self.variables = {}

    """
    ? Método que obtiene un arból de parseo.
    * Asímismo guarda el diccionario de variables creado por la clase Semantic.
    * En caso de encontrar algo no existente en la gramática, se cierra la ejecución del programa
    * y se indica el erro al usuario.
    """
    def getParseTree(self):
        semantic = Semantic(mode = False)

        parser = Lark(grammar, parser="lalr", transformer=semantic)

        try:
            self.parseTree = parser.parse("%s\n"%self.fileContents)
            #print(self.parseTree)
            self.variables = semantic.variables

        except UnexpectedInput as e:
            quit("%s"%e)

    """
    ? Método que obtiene todas las instancias de un token en un arból de parseo
    * Utiliza un método de pre-órden para recorrer el arból y obtener los tokens
    * pedidos por su valor y typo de token. Se extrae el número de línea y se guarda
    * en un arreglo.
    @param: tree Objeto del Arból de parseo
    @param: type Tipo de token a buscar
    @param: value Valor o literal que se busca
    @return results Arreglo con los números de línea pertenecientes al token
    """
    def getTokenInstances(self, tree, type, value):
        results =[]
        if isinstance(tree, Tree):
            for child in tree.children:
                if isinstance(child, Tree):
                    childArray = getTokenInstances(child, type, value)
                    if len(childArray) > 0:
                        results += childArray
                elif isinstance(child, Token) and ( child.type == type and child.value == value):
                    results.append(child.line)
        elif isinstance(child, Token) and ( child.type == type and child.value == value):
            results.append(child.line)
        return results

    """
    ? Método que convierte de un arreglo a una cadena que representa una lista (con comma).
    """
    def listToString(self, list):
        result = ""

        arraySize = len(list)

        for i in range (arraySize-1):
            result += "%s%s"%(result, item)

            if i == (arraySize-2):
                result += "%s,"%result

        return result

    """
    ? Método que obtiene el valor de una variable y devuelve el tipo de dato en una tupla
    """
    def getType(self, value):
        varType = ""

        if re.match(r"\d+", value):
            varType = "INTEGER"
        
        elif re.match(r"\d+\.\d+", value) :
            varType = "FLOAT"

        elif re.match(r"\"[^\"]*\"", value) or re.match(r"'[^']*'", value):
            varType = "STRING"

        elif re.match(r"^true$", value) or re.match(r"^false$", value):
            varType = "BOOLEAN"

        elif re.match(r"^null$",value):
            varType = "NULL"

        return varType

    """
    ? Método principal que crea la tabla de símbolos.
    * Recibe los contenidos del archivo para obtener un arból de parseo.
    * Obtiene las instancias en las que se llamó a la variable (líneas).
    * Prepara todo en uan matríz bidimensional para su impresión.
    @param: fileContents Los contenidos del archivo
    """
    def createTable(self, fileContents):
        self.fileContents = fileContents

        self.getParseTree()

        for variable, value in self.variables.items():
            row = []
            print(value)
            #varType = self.getType(value)
            #instances = self.getTokenInstances(self.parseTree, "IDENTIFIER", value)

            row.append(variable)
            #row.append(instances[0])
            #row.append( self.listToString(instances[1:]) )
            row.append(value)
            row.append("varType")

            self.symbolTable.append(row)

        return self

    """
    ? Método que imprime la tabla de símbolos
    * Primero imprime el encabezado con la información general del
    * programa (entre saltos de lína y utilizando tabulate para un mejor ordén).
    * Finalmente imprime la tabla creada a partir del llamado de métodos anteriores.
    """
    def printTable(self):
        print("\n"*2)
        print(tabulate(self.header, stralign="center", tablefmt="fancy_grid"))
        print("\n"*2)
        print(
            tabulate(
                self.symbolTable,
                #headers=["Nombre:", "Creada en:","Referencias:", "Valor:", "Tipo de Dato:"],
                headers=["Nombre:", "Valor:", "Tipo de Dato:"],
                tablefmt="grid",
                stralign="center"
            )
        )