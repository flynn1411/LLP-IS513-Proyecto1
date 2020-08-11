# -*- coding: utf-8 -*-

from Core.recognizer import Recognizer
from Core.tableCreator import TableCreator
from Core.FileReader import FileReader
import sys, re

arguments = sys.argv[1:]

fileReader = FileReader()

if len(arguments) == 1:
    #Lo de Gabriel y Fernando
    pass

elif len(arguments) == 2:
    #verificar parámetros
    command, fileName = arguments[0], arguments[1]

    #Crear tabla de simbólos
    if (
        re.match(r"--symbols-table", command) and
        re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
    ):
        fileContents = fileReader.readFile(fileName)
        (TableCreator()).createTable("%s"%fileContents).printTable()

    #Reconocimiento de lenguajes
    elif (
        re.match(r"--what-language-is-this", command) and
        re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
    ):
        fileContents = fileReader.readFile(fileName)
        (Recognizer()).recognize("%s\n" % fileContents).printResult()

else:
    quit("Error: Argumentos no válidos.")