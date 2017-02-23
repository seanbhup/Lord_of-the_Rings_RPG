class Fellowship_Of_The_Ring(object):
    def __init__(self,name,race,health,speed,strength,weapon,weapon_power):
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.strength = strength
        self.weapon = weapon
        self.weapon_power = weapon_power
    def help_frodo(self):
        print "You can do it Frodo. Trust " + self.name + "!"
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

Aragorn = Fellowship_Of_The_Ring("Aragorn","Human",50,8,9,"Anduril",8)
Gimli = Fellowship_Of_The_Ring("Gimli","Dwarf",50,5,10,"Battle Axe",7)
Frodo = Fellowship_Of_The_Ring("Frodo","Hobbit",50,7,6,"Sting",6)
Gandalf = Fellowship_Of_The_Ring("Gandalf","Wizard",50,8,10,"Glamdring & Wizard Staff",10)
Samwise_Gamgee = Fellowship_Of_The_Ring("Samwise","Hobbit",50,5,10,"Barrow Blade",5)
Boromir = Fellowship_Of_The_Ring("Boromir","Human",50,7,8,"Sword & Shield",7)
Faramir = Fellowship_Of_The_Ring("Faramir","Human",50,8,7,"Sword & Shield",7)
Merry_Brandybuck = Fellowship_Of_The_Ring("Merry","Hobbit",50,9,5,"Noldorin dagger",5)
Pippin_Took = Fellowship_Of_The_Ring("Pippin","Hobbit",50,9,5,"Troll's bane",6)
Legolas_Greenleaf = Fellowship_Of_The_Ring("Legolas","Elf",50,10,9,"Bow of the Galadhrim",9)
Smeagle = Fellowship_Of_The_Ring("Smeagle","Mutated Hobbit",50,7,6,"Passion for the Ring",10)
Drew_Parker = Fellowship_Of_The_Ring("Drew","Human",50,6,6,"Narsil",10)
