class School:

    def __init__(self,name,color,branches,classes,fees):
        print("this is a constructor") 
        self.name=name
        self.color=color
        self.branches=branches
        self.classes=classes
        self.fees=fees

    def houses(self):
        print("housecolors are","","","","")
    def  ranking_of_school(self):
        print("Best school in chromepet")

school1=School("shikshaa public school","white",5,"1 to 12",63000)
print(school1.color)          

