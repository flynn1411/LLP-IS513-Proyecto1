# -*- coding: utf-8 -*-

from Core.recognizer import *
import sys, re

arguments = sys.argv[1:]

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
        pass

    #Reconocimiento de lenguajes
    elif (
        re.match(r"--what-language-is-this", command) and
        re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
    ):
        f = open(fileName, "r")
        fileContents = f.read()
        f.close()

        (Recognizer()).recognize("%s\n" % fileContents).printResult()

else:
    quit("Error: Argumentos no válidos.")