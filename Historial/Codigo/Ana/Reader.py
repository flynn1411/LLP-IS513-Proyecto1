class Reader:
    def  __init__ ( self ):
        pass

    def  read ( self ):
        self.text = []
        try:
            text  =  input ()
            while  True :
                self.text  += [text]
                text  =  input ()
        except  EOFError :
            pass
        self.text  =  "\n".join(self.text)
        return self
    
    def read2(self,param):
        self.text = []

        fileName = param[0]
        f = open(fileName, "r")
        text = f.read()
        f.close()
        self.text += [text]

        self.text = "\n".join(self.text) 
        return self