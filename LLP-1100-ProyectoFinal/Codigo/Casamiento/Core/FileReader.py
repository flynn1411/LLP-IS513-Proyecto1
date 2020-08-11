# -*- coding: utf-8 -*-

class FileReader:
    def __init__(self): pass

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