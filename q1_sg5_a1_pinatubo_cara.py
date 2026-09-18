class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        
    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp=0
            
arthur = Hero("Arthur", 100)
morgan = Hero("Morgan", 100)
arthur.take_damage(10)

print(f"Arthur's HP: {arthur.hp}")
print(f"Morgan's HP: {morgan.hp}")
