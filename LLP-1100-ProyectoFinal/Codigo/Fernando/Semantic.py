# -*- coding: utf-8 -*-

import re
from lark import Transformer,v_args

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self):
        self.variables = {}
    
    def assigvar(self,name,value):
        self.variables[name] = value
    
    def print(self,item):
        print(item)
    
    def sum(self, valueA, valueB):
        print(valueA)
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if (typeA == "float" and typeB == "flaot"):
            return valueA + valueB
    
    def parseToken(self,value):

        if(re.match(r"/\d+(\.\d+)?/",value)):
            return (float(value),"float")

        elif(re.match(r"/\"[^\"]*\"/",value)):
            return ("%s"%value,"string")
        
        elif(re.match(r"/true/",value)):
            return (True,"bool")

        elif(re.match(r"/false/",value)):
            return (False,"bool")
        
        elif(re.match(r"/null/",value)):
            return (None,"null")

    def getvar(self,name):
        return self.variables[name]