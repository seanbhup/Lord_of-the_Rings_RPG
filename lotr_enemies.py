import math

# fighting_power_formula = (speed + (strength * weapon_power) * (math.pi / math.pi) - ((.5 * physical_resist) + (.5 * magic_resist))

class Anti_FellowShip(object):
    def __init__(self,name,race,health,speed,strength,weapon,weapon_type,weapon_power,physical_resist,magic_resist):
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.strength = strength
        self.weapon = weapon
        self.weapon_type = weapon_type
        self.weapon_power = weapon_power
        self.physical_resist = physical_resist
        self.magic_resist = magic_resist
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# weapon type 0 = physical, type 1 = magic, type 2 = hybrid
# name, race, health, speed, strength, weapon, weapon_type, weapon_power, physical_resist, magic_resist
Orc_Grunt = Anti_FellowShip("Zok","Orc",5,2,2,"Rusty Dagger","Physical",2,3,1)
Cave_Troll = Anti_FellowShip("Pateesa","Troll",6,2,9,"Giant Club","Physical",8,9,2)
Lurtz = Anti_FellowShip("Lurtz","Uruk-hai",50,7,7,"Sword & Shield","Physical",8,8,3)
Nazgul = Anti_FellowShip("Nazgul","Ring Wraith",100,10,9,"Black Mace","Physical",9,9,8)
Balrog = Anti_FellowShip("Balrog","Valarauka",200,7,10,"Fire","Magic",10,9,9)
Gollum = Anti_FellowShip("Smeagle","Mutated Hobbit",50,7,6,"Passion for the Ring","Magic",10,7,5)
Saruman = Anti_FellowShip("Saruman","Wizard",50,5,8,"Wizard Staff & Dark Sorcery","Magic",9,6,9)
Sauron = Anti_FellowShip("Sauron","Maiar",500,10,10,"The One Ring","Hybrid",20,20,20)
