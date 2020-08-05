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
    
#! Constructor 
    def __init__(self):
    #?Contenedores 
        self.variables = {}
        self.instructions = {}
   
#! Assignar valores a una variable 
    def assigvar(self,name,value):

    #Verifica el tipo de variable 
        value,typeVal = self.parseToken(value)

        if (typeVal == "string"):
            self.variables[name] = self.cleanParam(value)
        else:
            self.variables[name] = value
        
        return value

#! console.log de Java script
    def print(self,*item):
       
        item = "%s"%item

    #Verifica el tipo de variable 
        item,typeVal = self.parseToken(item)

        if (typeVal == "string"):
            print(self.cleanParam(item))
        else:
            print(item)
            
#! console.err de Java script
    def printerr(self,item):

        item = "%s"%item

    #Verifica el tipo de variable 
        item,typeVal = self.parseToken(item)

    #Color a los print
        if (typeVal == "string"):
            print("\033[1 %s \033[0m" %self.cleanParam(item))
        else:
            print("\033[1;31;1m %s \033[0m" %item)

#! Comparar si dos valores son iguales 
    def equal(self,valueA,valueB):

    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA == valueB:
                return "true"
            else:
                return "false"

#! Comparar si un valor es mayor/igual que otro  
    def greaterequal(self,valueA,valueB):

    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA >= valueB:
                return "true"
            else:
                return "false"
                
#! Comparar si un valor es menor/igual que otro  
    def lesserequal(self,valueA,valueB):

    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA <= valueB:
                return "true"
            else:
                return "false"

#! Comparar si un valor es mayor que otro  
    def greater(self,valueA,valueB):
    
    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA > valueB:
                return "true"
            else:
                return "false"

#! Comparar si un valor es menor que otro  
    def lesser(self,valueA,valueB):
    
    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)

        if ((typeA == "float") and (typeB == "float")):
            if valueA < valueB:
                return "true"
            else:
                return "false"

#! Suma de dos valores y concatenar cadenas   
    def sum(self, valueA, valueB):
    
    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA + valueB

        elif ((typeA == "string") and (typeB == "string")):
            return "%s%s"%(valueA,valueB) 

#! Resta de dos valores  
    def sub(self, valueA, valueB):

    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA - valueB

#! Multiplicacion de dos valores  
    def mul(self, valueA, valueB):
    
    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA * valueB

#! Division de dos valores  
    def div(self, valueA, valueB):
    
    #Verifica el tipo de variable 
        valueA,typeA = self.parseToken(valueA)
        valueB,typeB = self.parseToken(valueB)
        
        if ((typeA == "float") and (typeB == "float")):
            return valueA / valueB

#! Verificador de variables 
    def parseToken(self,value):
        
        #? Verifica enteros o Floantes 
        if ((type(value) == float) or (re.match(r"\d+(\.\d+)?",value))):
            return (float(value),"float")
        
        #? Verifica booleano Verdadero 
        elif(re.match(r"^true$",value)):
            return ("true","bool")

        #? Verifica booleano Falso 
        elif(re.match(r"^false$",value)):
            return ("false","bool")
        
        #? Verifica nulos
        elif(value == "null"):
            return ("null","null")

        #? Verifica cadenas 
        elif ((type(value) == str) or (re.match(r"\"[^\"]*\"",value)) or (re.match(r"'[^']*'",value))):
            return ("%s"%self.cleanParam(value),"string")

        else:
            return ("Error No match variable")
            
#! Obtener valores de variables  
    def getvalue(self,name):

        #Verifica si es palabra reservada
        if self.iskeyword(name):
            value, _ = self.parseToken(name)
            return value

        return self.variables[name]

#! Limpiar caracteres incesesarios de una cadena  
    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            
            #reconocer caracteres especiales dentro de una cadena
            param = re.sub(r"\\n","\n" , param)
            param = re.sub(r"\\t","\t" , param)

            return param[1:-1]
        return param

#! Validacion de palabras reservadas   
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

#! Guardar los parametros de una funcion
    def saveparams(self,param1, param2):
        parameters = []
        if(param1 and param2):            
            if( type(param2) == list ):
                parameters = param2[:]
                parameters += [str(param1)]

            else:
                parameters = [str(param2), str(param1) ]
        
        return parameters

#! Guardar instrucciones de una funcion
    def savefun(self, name, params, instructions):
        if type(params) == list:
            params.reverse()
        self.instructions[name] = {}
        self.instructions[name]["instructions"] = instructions
        self.instructions[name]["params"] = params

#! Limpiar las instrucciones de una funcion
    def parsefun(self, expresions):
        return ("%s" % expresions).strip()

#! Ejecucuion de una funcion
    def exefun(self, name, arguments):
        
        if type(arguments) == list:
            arguments.reverse()

        text = self.instructions[name]["instructions"]
        parameters = self.instructions[name]["params"]
        add = ""

        for i in range(len(parameters)):
            add += "%s = %s;\n"%(parameters[i],arguments[i])     

        text = "%s%s"%(add,text)

        #? Ejecutar las instrucciones
        self.subProgram(text)
    
    #def rtn(self,expersion):
        #return expersion

#! Obtener el tamaño de una cadena o numero
    def length(self,value):
        return len(value)
    
#! Codicional if 
    def ifstmt(self,condition,instructions):
        
        if condition == "true": 
            #? Ejecutar instrucciones del If
            self.subProgram(instructions)
        else:
            pass

#! Codicional if else
    def ifelsestmt(self,condition,ifInstructions,elseInstructions):
        
        if condition == "true": 
            #? Ejecutar instrucciones del If
            self.subProgram(ifInstructions)
        else:
            #? Ejecutar instrucciones del Else
             self.subProgram(elseInstructions)

#! Subprograma para ejecutar instrucciones
    def subProgram(self,text):
        
        #? llamado recursivo
        parser = Lark(grammar,parser="lalr",transformer=self)
        language = parser.parse

        sample = text
        try:
            language(sample)
        except Exception as e:
            print("Error: %s" % e)

#! Bucle For
    def forstmt(self,exp,condition,increment,instruccion):
    
        a = exp
        
        print(condition)
        print(increment)
        #print(instruccion)
        
        for i in range(int(exp)):
            self.subProgram(instruccion)                   