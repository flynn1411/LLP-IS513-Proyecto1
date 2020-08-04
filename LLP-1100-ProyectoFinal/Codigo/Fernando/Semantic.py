# -*- coding: utf-8 -*-

"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

import re
from lark import Transformer,v_args

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.instructions = {}
        self.params = None
   
    def assigvar(self,name,value):
        value,typeVal = self.parseToken(value)
      
        if (typeVal == "string"):
            self.variables[name] = self.cleanParam(value)
        
        else:
            self.variables[name] = value
    
    def print(self,item):
        print(item)
    
    def equal(self,valueA,valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA == valueB:
                return "true"
            else:
                return "false"
    def greaterequal(self,valueA,valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA >= valueB:
                return "true"
            else:
                return "false"
                
    def lesserequal(self,valueA,valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA <= valueB:
                return "true"
            else:
                return "false"

    def greater(self,valueA,valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA > valueB:
                return "true"
            else:
                return "false"

    def lesser(self,valueA,valueB):
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA < valueB:
                return "true"
            else:
                return "false"

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
        
        elif(re.match(r"^true$",value)):
            return ("true","bool")

        elif(re.match(r"^false$",value)):
            return ("false","bool")
        
        elif(value == "null"):
            return ("null","null")

        elif ((type(value) == str) or (re.match(r"\"[^\"]*\"",value)) or (re.match(r"'[^']*'",value))):
            return ("%s"%self.cleanParam(value),"string")

        else:
            return ("Error","Error")

    def getvalue(self,name):

        if self.iskeyword(name):
            value, _ = self.parseToken(name)
            return value

        return self.variables[name]

    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            
            #reconocer caracteres especiales dentro de una cadena
            param = re.sub(r"\\n","\n" , param)
            param = re.sub(r"\\t","\t" , param)

            #print(param)
            return param[1:-1]
        return param

    def iskeyword(self, value):
        if( 
            re.match(r"^true$", value) or
            re.match(r"^false$", value) or
            re.match(r"^null$", value) 
        ):
            return True

    def arguments(self, val1, val2):
        if(type(val2) == list ):
            parameters = val2[:]
            if(val1 in self.variables.keys()):
                val1 = self.getvalue(val1)
            parameters += [val1]
        
        else:
            
            if(val1 in self.variables.keys()):
                val1 = self.getvalue(val1)

            if(val2 in self.variables.keys()):
                val2 = self.getvalue(val2)
            
            parameters = [val2, val1 ]
        
        return parameters

    def parameters(self,param1, param2):
        if( type(param2) == list ):
            parameters = param2[:]
            parameters += [param1]

        else:
            parameters = [param2, param1 ]
        
        return parameters


    def fun(self, name, param, instructions):
        self.instructions[name] = {instructions}
        print(self.instructions[name])


    def savefun(self, expresions):
        return ("%s" % expresions).strip()

