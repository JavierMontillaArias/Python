#OOP
class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age
    
    def run (self):
        print('run')

player1 = PlayerCharacter('Harry', 18)
player2 = PlayerCharacter('Ron', 17)
player2.attacck = 50

print(player1.name)
print(player2.membership)