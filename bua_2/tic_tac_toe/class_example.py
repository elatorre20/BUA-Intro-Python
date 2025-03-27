class exampleClass():
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return(self.name + ',' + str(self.number))
    
    def change_name(self, newname):
        self.name = newname
        return(self.name)
        
