# Class 02 :

class Mess:
    
    def __init__(self,mess_name,type):
        self.m_name=mess_name
        self.type=type

mess1=Mess("Shiv_Samarth_Bhojnalaya","veg")
mess2=Mess("Khandesh_katta","veg")

print("mess name :", mess1.m_name)
print("mess type :", mess1.type)

print("mess name :",mess2.m_name)
print("mess type :",mess2.type)