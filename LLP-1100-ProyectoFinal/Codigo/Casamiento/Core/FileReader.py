# -*- coding: utf-8 -*-

"""
! Lector de archivos
? Contiene un sólo método que lee los contenidos de un archivo.
* Devuelve error de suceder.
* Exista o no un error, se cierra el flujo de datos entre el archivo y el programa.
@author: flynn1411
@version: 0.1
@date: 10/08/2020
"""
class FileReader:
    def __init__(self): pass

    #Método para leer los contenidos de un archivo
    def readFile(self, fileName):
        fileContents = ""

        try:
            userFile = open(fileName, "r")
            fileContents = userFile.read()
            
        except Exception as e:
            quit("Error en la lectura del archivo:\n\n%s"%e)

        finally:
            userFile.close()

        return fileContents