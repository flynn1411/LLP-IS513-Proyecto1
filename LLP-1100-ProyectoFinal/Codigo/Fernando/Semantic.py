# -*- coding: utf-8 -*-

"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""

import re
from lark import Lark,Transformer,v_args
from Grammar import *

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.instructions = {}
   
    def assigvar(self,name,value):
        value,typeVal = self.parseToken(value)
        
        if (typeVal == "string"):
            self.variables[name] = self.cleanParam(value)
        
        else:
            self.variables[name] = value
    
    def print(self,item):
        
        item = "%s"%item
        item,typeVal = self.parseToken(item)

        if (typeVal == "string"):
            print(self.cleanParam(item))
        else:
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

    def sendarguments(self, val1, val2):
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

    def saveparams(self,param1, param2):
        parameters = []
        if(param1 and param2):            
            if( type(param2) == list ):
                parameters = param2[:]
                parameters += [str(param1)]

            else:
                parameters = [str(param2), str(param1) ]
        
        return parameters

    def savefun(self, name, params, instructions):
        if type(params) == list:
            params.reverse()
        self.instructions[name] = {}
        self.instructions[name]["instructions"] = instructions
        self.instructions[name]["params"] = params
  
    def parsefun(self, expresions):
        return ("%s" % expresions).strip()

    def exefun(self, name, arguments):
        
        if type(arguments) == list:
            arguments.reverse()
        text = self.instructions[name]["instructions"]
        parameters = self.instructions[name]["params"]
        add = ""
        for i in range(len(parameters)):
            add += "%s = %s;\n"%(parameters[i],arguments[i])     

        text = "%s%s"%(add,text)
        self.subProgram(text)
    
    #def rtn(self,expersion):
        #return expersion

    def length(self,value):
        return len(value)
    
    def ifstmt(self,condition,instructions):
        
        if condition == "true": 
            self.subProgram(instructions)
        else:
            pass

    def ifelsestmt(self,condition,ifInstructions,elseInstructions):
        
        if condition == "true": 
            self.subProgram(ifInstructions)
        else:
             self.subProgram(elseInstructions)

    def subProgram(self,text):

        parser = Lark(grammar,parser="lalr",transformer=self)
        language = parser.parse

        sample = text
        try:
            language(sample)
        except Exception as e:
            print("Error: %s" % e)
        