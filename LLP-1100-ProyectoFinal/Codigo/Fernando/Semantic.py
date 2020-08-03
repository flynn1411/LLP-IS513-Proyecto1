# -*- coding: utf-8 -*-

import re
from lark import Transformer,v_args

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self):
        self.variables = {}
    
    def assigvar(self,name,value):
        value,typeVal = self.parseToken(value)

        if (typeVal == "string"):
            self.variables[name] = self.cleanParam(value)

        self.variables[name] = value
    
    def print(self,item):
        print(item)
    
    def sum(self, valueA, valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA + valueB

        elif ((typeA == "string") and (typeB == "string")):
            return "%s%s"%(valueA,valueB) 

    def sub(self, valueA, valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA - valueB

    def mul(self, valueA, valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA * valueB

    def div(self, valueA, valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA / valueB
    
    def parseToken(self,value):

        if ((type(value) == float) or (re.match(r"\d+(\.\d+)?",value))):
            return (float(value),"float")

        elif ((type(value) == str) or (re.match(r"\"[^\"]*\"",value)) or (re.match(r"'[^']*'",value))):
            return ("%s"%self.cleanParam(value),"string")
        
        elif(re.match(r"true",value)):
            return (True,"bool")

        elif(re.match(r"false",value)):
            return (False,"bool")
        
        elif(re.match(r"null",value)):
            return (None,"null")

        else:
            return ("Error","Error")

    def getvar(self,name):
        return self.variables[name]

    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            
            #reconocer caracteres especiales dentro de una cadena
            param = re.sub(r"\\n","\n" , param)
            param = re.sub(r"\\t","\t" , param)

            #print(param)
            return param[1:-1]
        return param