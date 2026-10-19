# Class 01 :
 
class Pmpml:                                #Class

    def __init__(self,b_no,b_route):        #Constructor
        self.b_no=b_no
        self.bus_route= b_route

bus1=Pmpml(98,"Wagholi")                    #Object
bus2=Pmpml(43,"Katraj")
bus3=Pmpml(276,"ChinchwadGaon")

print("Bus Number :",bus1.b_no)
print("Bus route :",bus1.bus_route)

print("Bus Number :",bus2.b_no)
print("Bus route :",bus2.bus_route)

print("Bus Number :",bus3.b_no)
print("Bus route :",bus3.bus_route)