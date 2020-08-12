# -*- coding: utf-8 -*-

from Core.recognizer import Recognizer
from Core.JavaScript import JavaScript
from Core.tableCreator import TableCreator
from Core.FileReader import FileReader
import re

class MainProgram:
	def __init__(self):
		pass

	def checkArguments(self, arguments):
		if len(arguments) == 1:

			#Caso para ejecutar argumentos
		    if re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}", arguments[0]):
		        fileContents = (FileReader()).readFile(arguments[0])
		        (JavaScript()).runCode(fileContents)

		    #Caso para mostrar los comandos posibles a utilizar
		    elif re.match(r"--help", arguments[0]):
		        print("""
Uso del interprete de lenguajes Rosetta:
python3 main.py  <filePath> : Ejecutar código de JavaScript dada la ruta a un archivo.
\t\t [--symbols-table] <filePath> : Mostrar la tabla de símbolos generada internamente para la ejecución de código JavaScript, dada la ruta hacía un archivo.
\t\t [--what-language-is-this] <filePath> : Detectar gramáticalmente el lenguaje de programación de un software, dada la ruta hacía un archivo.
\t\t [--version] : Muestra la información sobre el programa.
		        	""")

		    #Caso para mostrar los autores y sobre el programa
		    elif re.match(r"--version",arguments[0]):
		    	print("\n\n")

		    	#Arte ASCII creado en: https://onlineasciitools.com/convert-text-to-ascii-art
		    	print("""
............................................................................
:: ########:::'#######:::'######::'########:'########:'########::::'###:::::
:: ##.... ##:'##.... ##:'##... ##: ##.....::... ##..::... ##..::::'## ##::::
:: ##:::: ##: ##:::: ##: ##:::..:: ##:::::::::: ##::::::: ##:::::'##:. ##:::
:: ########:: ##:::: ##:. ######:: ######:::::: ##::::::: ##::::'##:::. ##::
:: ##.. ##::: ##:::: ##::..... ##: ##...::::::: ##::::::: ##:::: #########::
:: ##::. ##:: ##:::: ##:'##::: ##: ##:::::::::: ##::::::: ##:::: ##.... ##::
:: ##:::. ##:. #######::. ######:: ########:::: ##::::::: ##:::: ##:::: ##::
::..:::::..:::.......::::......:::........:::::..::::::::..:::::..:::::..:::
+-+-+-+-+-+-+-+-+-+-+-+-+
version 0.1  16-08-2020
+-+-+-+-+-+-+-+-+-+-+-+-+
		    		""")
		    	print("""
========================================
		Authors
========================================
		    		""")
		    	(JavaScript()).runCode("console.error(\"Authors\");")

		elif len(arguments) == 2:
		    #verificar parámetros
		    command, fileName = arguments[0], arguments[1]

		    #Crear tabla de simbólos
		    if (
		        re.match(r"--symbols-table", command) and
		        re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
		    ):
		        fileContents = (FileReader()).readFile(fileName)
		        (TableCreator()).createTable("%s"%fileContents).printTable()

		    #Reconocimiento de lenguajes
		    elif (
		        re.match(r"--what-language-is-this", command) and
		        re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
		    ):
		        fileContents = (FileReader()).readFile(fileName)
		        (Recognizer()).recognize("%s\n" % fileContents).printResult()

		else:
		    print("Error: Argumentos no válidos.\nIngrese \"--help\" si desea conocer los comandos disponibles.")