# -*- coding: utf-8 -*-

"""
    @author Fernando y Gabriel
    @date 03-08-2020
    @version 0.1
"""
import random
import re
from lark import Lark,Transformer,v_args
from Grammar import *

@v_args(inline=True)


class Semantic(Transformer):
    
#! Constructor 
    def __init__(self, rgb = False, mode = True):
    #?Contenedores 
        self.variables = {}
        self.functions = {}
        self.returnValue = None
        self.rgb = rgb
        self.mode = mode
   
#! Assignar valores a una variable 
    def assigvar(self,name,value):
    #Verifica el tipo de variable 
        value,typeVal = self.parseToken(value)
        if (typeVal == "string"):
            self.variables[name] = self.cleanParam(value)
        else:
            self.variables[name] = value
        
        return name

#! console.log de Java script
    def print(self,*item):
        if self.mode:
            item = "%s"%item

        #Verifica el tipo de variable 
            item,typeVal = self.parseToken(item)

            if (typeVal == "string"):
                print(self.cleanParam(item))
            else:
                print(item)

    def concat(self, var1, var2):
       
        if var1 in self.variables.keys():
            var1 = self.variables[var1]
        else:
            var1,_ = self.parseToken(var1)
        
        if var2 in self.variables.keys():
            var2 =self.variables[var2]
        else:
            var2,_ = self.parseToken(var2)
            
        return "%s %s" % (var1, var2)

#! console.err de Java script
    def printerr(self,item):
        if self.mode:
            item = "%s"%item
            color = 31
            array = [31,32,33,34,35,36]
            if self.rgb:
                color = random.choice(array) 

            
        #Verifica el tipo de variable 
            item,typeVal = self.parseToken(item)

        #Color a los print
            if(item == "Authors"):
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"Nombre\t\t|\tNumero de cuenta"))
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"-"*40))
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"Ana Hernández\t|\t20171001620"))
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"Fernando Cortés\t|\t20171030809"))
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"Gabriel Escobar\t|\t20181005735"))
                print("\033[1;%s;40m%s \033[0m" %(random.choice(array),"Josue Izaguirre\t|\t20171034157"))
                
            
            elif (typeVal == "string"):
                print("\033[1;%s;1m %s \033[0m" %(color,self.cleanParam(item)))

            else:
                print("\033[1;%s;1m %s \033[0m" %(color,item))

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
        if ((type(value) == float) or (type(value) == int) or (re.match(r"\d+(\.\d+)?",value))):
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

#! retornar valores vacios
    def none(self):
        return None

#! Guarda los argumentos de la ejecucion de una función
    def sendargument(self,arg):
        val,_ = self.parseToken(arg)
        return [val]

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

#! Guardar los parametros de la declaración de una funcion
    def saveparam(self, param):
        return ["%s"%param]
    
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
        self.functions[name] = {}
        self.functions[name]["instructions"] = instructions
        self.functions[name]["params"] = params

#! Limpiar las instrucciones de una funcion
    def parsefun(self, expresions):
        #print("---------"*5)
        #print(expresions)
        return ("%s" % expresions).strip()

#! Ejecucuion de una funcion
    def exefun(self, name, arguments):
        if type(arguments) == list:
            arguments.reverse()

        text = self.functions[name]["instructions"]
        parameters = self.functions[name]["params"]
        add = ""

        if(type(parameters) == list):
            for i in range(len(parameters)):
                add += "%s = %s;\n"%(parameters[i],arguments[i])     

        text = "%s%s"%(add,text)

    #? Ejecutar las instrucciones
        
        try:
            self.subProgram(text)
        except Exception as e:

            if ("%s" % e == 'Exit'):
                pass
            else:
                print("funError: %s" % e)
    
        returnValue = self.returnValue
        self.returnValue = None

        return returnValue

#! Obtener el tamaño de una cadena o numero
    def length(self,value):
        value = "%s"%value
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
            if ("%s" % e == 'Exit'):
                raise Exception("Exit")
            else:
                print("subError: %s" % e)

#! While
    
    def whilestmt(self,condition,instruccion):

        if type(condition) == tuple:
           
            var = condition[0]
            con = condition[1]
            var2 = condition[2]

            varValue = condition[0]
            varValue2 = condition[2]
            
            if( type(var) == str):
                varValue = self.variables[var]

            if( type(var2) == str):
                varValue2 = self.variables[var2]
            
        
            keep = self.conditionalEval(varValue,con,varValue2)

            while(keep):

                self.subProgram(instruccion)
                
                varValue = condition[0]
                varValue2 = condition[2]
            
                if( type(var) == str):
                    varValue = self.variables[var]

                if( type(var2) == str):
                    varValue2 = self.variables[var2]

                keep = self.conditionalEval(varValue,con,varValue2)          

        

        else:
            var = condition
            varValue = self.variables[var]

            if varValue == 'true': 
                keep = True
            else: 
                keep = False
                
            while(keep):
                self.subProgram(instruccion)
                varValue = self.variables[var]
                if varValue == 'true': 
                    keep = True
                else: 
                    keep = False
        
    def condionwhilecomp(self,var,con,var2):
        var = "%s"%var
        con = "%s"%con
        var2 = "%s"%var2

        var,_ = self.parseToken(var)
        con,_ = self.parseToken(con)
        var2,_ = self.parseToken(var2)


        return (var,con,var2)
        

    def condionforcomp(self, var1, cond, var2):
        
        return (int(var1),cond,int(var2))

    def logicalequal(self):
        return "=="

    def logicalmorethan(self):
        return ">="

    def logicallessthan(self):
        return "<="

    def logicalmore(self):
        return ">"

    def logicalless(self):
        return "<"


#! Bucle For
    def forstmt(self,nameVar,condition,increment,instruccion):

        logSymbol = condition[1]
        changingVar = self.variables[nameVar]
        
        if(changingVar == condition[2]):
            untilVar = condition[0]
        else:
            untilVar = condition[2]
        
        keep = self.conditionalEval(changingVar, logSymbol, untilVar)

        while(keep):
            self.subProgram(instruccion)

            if(increment == "++"):
                changingVar += 1
                
            elif(increment == "--"):
                changingVar -= 1

            self.variables[nameVar] = changingVar
            keep = self.conditionalEval(changingVar, logSymbol, untilVar)
                
    
    def conditionalEval(self,var1, cond, var2):
        if(cond == "=="):
            if(not (var1 == var2)): return False
            
        elif(cond == "<="):
            if(not (var1 <= var2)): return False
           
        elif(cond == ">="):
           if(not (var1 >= var2)): return False
           
        elif(cond == "<"):
           if(not (var1 < var2)): return False

        elif(cond == ">"):
           if(not (var1 > var2)): return False

        return True

#! Incrementar 
    def incrementfor(self,name):
        return "++"
    
    def decrementfor(self,name):
        return "--"

    def parser_segment(self,*segments):
        
        text = " "
        for seg in segments:
            text += "{ %s }" % seg
    
        return text

    def joinsegments(self,*segments):
        text = " "
        for seg in segments:
            text += "%s" % seg
        return text

    def returnop(self, value):
        self.returnValue = value
        raise Exception("Exit")

    def increment(self,name):
        self.variables[name] = self.variables[name] + 1
    
    def decrement(self,name):
        self.variables[name] = self.variables[name] - 1