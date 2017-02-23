import math

# fighting_power_formula = (speed + (strength * weapon_power) * (math.pi / math.pi) - ((.5 * physical_resist) + (.5 * magic_resist));

class Fellowship_Of_The_Ring(object):
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
    def help_frodo(self):
        print "You can do it Frodo. Trust " + self.name + "!"
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# weapon type 0 = physical, type 1 = magic, type 2 = hybrid
# name, race, health, speed, strength, weapon, weapon_type, weapon_power, physical_resist, magic_resist
Aragorn = Fellowship_Of_The_Ring("Aragorn","Human",50,8,9,"Anduril","Hybrid",8,9,6)
Gimli = Fellowship_Of_The_Ring("Gimli","Dwarf",50,5,10,"Battle Axe","Physical",7,8,5)
Frodo = Fellowship_Of_The_Ring("Frodo","Hobbit",50,7,6,"Sting","Hybrid",6,6,8)
Gandalf = Fellowship_Of_The_Ring("Gandalf","Wizard",50,8,10,"Glamdring & Wizard Staff","Hybrid",10,8,10)
Samwise_Gamgee = Fellowship_Of_The_Ring("Samwise","Hobbit",50,5,10,"Barrow Blade","Physical",5,6,7)
Boromir = Fellowship_Of_The_Ring("Boromir","Human",50,7,8,"Sword & Shield","Physical",7,7,4)
Faramir = Fellowship_Of_The_Ring("Faramir","Human",50,8,7,"Sword & Shield","Physical",7,8,6)
Merry_Brandybuck = Fellowship_Of_The_Ring("Merry","Hobbit",50,9,5,"Noldorin dagger","Physical",5,6,5)
Pippin_Took = Fellowship_Of_The_Ring("Pippin","Hobbit",50,9,5,"Troll's bane","Physical",6,6,5)
Legolas_Greenleaf = Fellowship_Of_The_Ring("Legolas","Elf",50,10,9,"Bow of the Galadhrim","Physical",9,9,8)
Smeagle = Fellowship_Of_The_Ring("Smeagle","Mutated Hobbit",50,7,6,"Passion for the Ring","Magic",10,7,5)
Drew_Parker = Fellowship_Of_The_Ring("Drew","Human",50,6,6,"Narsil","Physical",10,10,10)
