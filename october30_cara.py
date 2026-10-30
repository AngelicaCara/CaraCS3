
class Character:
    def special_move(self):
        pass
        

    def special_move(self):
        print("Character", special_move, "!")

class Warrior(Character):
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage(Character):
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer(Character):
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()
    

warrior= Warrior()
mage = Mage()
archer=Archer()

characters = [warrior, mage ,archer]

for char in characters:
    perform_move(char)
