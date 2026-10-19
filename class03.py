#Class 03

class TeaHouse:

    def __init__(self,n,p):
        self.name=n
        self.price=p
    
tea=TeaHouse("IT_Chaha_Wala",15)
coffee=TeaHouse("IT_Coffee_Wala",20)

print("Shop Name :",tea.name)
print("Price :",tea.price)

print("Shop Name :",coffee.name)
print("Price :",coffee.price)