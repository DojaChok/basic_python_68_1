"""
#
# Fuctions
#
"""
def myFullName(firstName = "unknow", lastName = "forger"):
    return firstName + " " + lastName

print(myFullName("Lion", "Diet"))
print(myFullName(""))
print(myFullName(lastName="Smith"))  
print(myFullName(firstName="John", lastName="Doe"))  
print(myFullName())  # using default parameters

def redpotion(hp):
    return hp + 50
def bluepotion(mp):
    return mp + 30

current_hp = 100
print("Current HP:", current_hp)
current_hp = redpotion(current_hp)
print("After red potion, HP:", current_hp)