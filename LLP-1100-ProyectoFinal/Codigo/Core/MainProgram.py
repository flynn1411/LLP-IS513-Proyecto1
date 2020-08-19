# -*- coding: utf-8 -*-

from Core.recognizer import Recognizer
from Core.JavaScript import JavaScript
from Core.tableCreator import TableCreator
from Core.FileReader import FileReader
import re

"""
! Clase Principal
? Maneja las instrucciones y argumentos recibidos por el usuario para asegurar la ejecución debida de su funcionalidad.
* Contiene un manual de uso al ingresar '--help' como único parámetro.
* Contiene un comando para mostrar información sobre el programa (Nombre del software, versión, fecha y autores).
? Dentro de su funcionalidad principal se encuentra:
* Ejecutar código de JavaScript (limitado a un pequeño grupo de instrucciones y operaciones enlistadas en la definición del proyecto).
* Mostrar la tabla de símbolos utilizada para la ejecución interna del código JavaScript
* Reconocer gramáticalmente el código de algún software del lenguaje Ruby o Bash (limitado a un pequeño grupo de instrucciones y
* operaciones enlistadas en la definición del proyecto).
@author: flynn1411
@version: 0.2
@date: 11/08/2020
"""
class MainProgram:
	def __init__(self):
		pass

	"""
	! Método principal para procesar los argumentos ingresados por el usuario.
	"""
	def checkArguments(self, arguments):
		if len(arguments) == 1:

			#Caso para ejecutar código JS
			if re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}", arguments[0]):
				fileContents = (FileReader()).readFile(arguments[0])
				(JavaScript()).runCode(fileContents)

			#Caso para mostrar los comandos posibles a utilizar
			elif re.match(r"--help", arguments[0]):
				print("""
Uso del interprete de lenguajes Rosetta:
python3 main.py  <filePath> : Ejecutar código de JavaScript dada la ruta a un archivo.\n
\t\t [--rgb-mode] <filePath> : Ejecutar código de JavaScript dada la ruta a un archivo, con un toque de colores.\n
\t\t [--symbols-table] <filePath> : Mostrar la tabla de símbolos generada internamente para la ejecución de código JavaScript, dada la ruta hacía un archivo.\n
\t\t [--what-language-is-this] <filePath> : Detectar gramáticalmente el lenguaje de programación de un software, dada la ruta hacía un archivo (solo detecta Ruby y Bash).\n
\t\t [--info] : Muestra la información sobre el programa.
				""")

			#Caso para mostrar los autores y sobre el programa
			elif re.match(r"--info",arguments[0]):

				#Arte ASCII creado en: https://onlineasciitools.com/convert-text-to-ascii-art
				arte = """
............................................................................
::'########:::'#######:::'######::'########:'########:'########::::'###:::::
:: ##.... ##:'##.... ##:'##... ##: ##.....::... ##..::... ##..::::'## ##::::
:: ##:::: ##: ##:::: ##: ##:::..:: ##:::::::::: ##::::::: ##:::::'##:. ##:::
:: ########:: ##:::: ##:. ######:: ######:::::: ##::::::: ##::::'##:::. ##::
:: ##.. ##::: ##:::: ##::..... ##: ##...::::::: ##::::::: ##:::: #########::
:: ##::. ##:: ##:::: ##:'##::: ##: ##:::::::::: ##::::::: ##:::: ##.... ##::
:: ##:::. ##:. #######::. ######:: ########:::: ##::::::: ##:::: ##:::: ##::
::..:::::..:::.......::::......:::........:::::..::::::::..:::::..:::::..:::"""

				print("""\033[1;36;50m%s\033[0m
+-+-+-+-+-+-+-+-+-+-+-+-+
version 0.1  16-08-2020
+-+-+-+-+-+-+-+-+-+-+-+-+
========================================
		Authors
========================================
"""%arte)
				(JavaScript()).runCode("console.error(\"Authors\");")
				print("\n"*2)
				
			#Caso desconocido
			else:
				print("Error: Argumentos no válidos.\nIngrese \"--help\" si desea conocer los comandos disponibles.\n")

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

			elif(
				re.match(r"--rgb-mode", command) and
				re.match(r"[a-zA-Z][a-zA-Z0-9_ ]*.[a-z]{1,6}",fileName)
			):
				fileContents = (FileReader()).readFile(fileName)
				(JavaScript(rgb=True)).runCode(fileContents)
			
			else:
				print("Error: Argumentos no válidos.\nIngrese \"--help\" si desea conocer los comandos disponibles.\n")

		else:
			print("Error: Argumentos no válidos.\nIngrese \"--help\" si desea conocer los comandos disponibles.\n")