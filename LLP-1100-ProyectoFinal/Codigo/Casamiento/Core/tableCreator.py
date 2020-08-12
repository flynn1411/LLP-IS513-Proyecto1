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
            ["Intérprete de Lenguajes Rosetta"],
            ["@authors:\nAna Hernández(its_anaehm),\nFernando Córtes(Ferloxc),\nGabriel Escobar(Lersgeeb),\nJosué Izaguirre (flynn1411)"],
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

        try:

            #Parseo para obtener la información de las varibales
            Lark(grammar, parser="lalr", transformer=semantic).parse("%s\n"%self.fileContents)
            self.variables = semantic.variableTable

            #Árbol completo para obtener los llamados a variables
            self.parseTree = (Lark(grammar, parser="lalr")).parse("%s\n"%self.fileContents)
            #print(self.parseTree)
            #print(self.variables)

        except UnexpectedInput as e:
            quit("%s"%e)

    def getReferences(self, id):
        pass

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
                    childArray = self.getTokenInstances(child, type, value)

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
    def listToString(self, arr):
        cleanedList = []

        for i in arr:

            #print(arr[i])

            if i in cleanedList:
                pass
            else:
                cleanedList.append(i)

        result = ""

        for item in cleanedList:
            result = "%s %s"%(result, item)
            #print(result)

        return result

    """
    ? Método que obtiene el valor de una variable y devuelve el tipo de dato
    """
    def getType(self, value):
        varType = ""

        if re.match(r"\d+", value):
            varType = "INTEGER"
        
        elif re.match(r"\d+\.\d+", value) :
            varType = "FLOAT"

        elif re.match(r"^true$", value) or re.match(r"^false$", value):
            varType = "BOOLEAN"

        elif re.match(r"^null$",value):
            varType = "NULL"
            
        else:
            varType = "STRING"
			
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

        for variable, info in self.variables.items():
            row = []
            value = "%s"%info["value"]
            varType = self.getType(value)

            if varType == "STRING":
                value = "\"%s\""%value

            elif varType == "INTEGER":
                value = int(float(value))

            instances = self.getTokenInstances(self.parseTree, "IDENTIFIER", variable)

            row.append(variable)

            if instances:
                row.append(instances[0])

                if len(instances)>1:
                    row.append( self.listToString(instances[1:]) )
                
                else:
                    row.append("-")
            
            else:
                row.append("-")
                row.append("-")

            row.append(value)
            row.append(varType)
            row.append(info["scope"])

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
        print(tabulate(self.header, tablefmt="fancy_grid"))
        print("\n\t\t\t\tTabla de Símbolos\n")
        print(
            tabulate(
                self.symbolTable,
                headers=["Nombre:", "Creada en:","Referencias:", "Valor:", "Tipo de Dato:", "Función:"],
                #headers=["Nombre:", "Valor:", "Tipo de Dato:"],
                tablefmt="grid",
                stralign="center",
                numalign="center"
            )
        )