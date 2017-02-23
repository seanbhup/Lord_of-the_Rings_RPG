class Anti_FellowShip(object):
    def __init__(self,name,race,health,speed,strength,weapon,weapon_power):
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.strength = strength
        self.weapon = weapon
        self.weapon_power = weapon_power
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

Orc_Grunt = Anti_FellowShip("Zok","Orc",5,2,2,"Rusty Dagger",2)
Cave_Troll = Anti_FellowShip("Pateesa","Troll",75,2,9,"Giant Club",8)
Lurtz = Anti_FellowShip("Lurtz","Uruk-hai",50,7,7,"Sword & Shield",8)
Nazgul = Anti_FellowShip("Nazgul","Ring Wraith",100,10,9,"Black Mace",9)
Balrog = Anti_FellowShip("Balrog","Valarauka",200,7,10,"Fire",10)
Gollum = Anti_FellowShip("Smeagle","Mutated Hobbit",50,7,6,"Passion for the Ring",10)
Saruman = Anti_FellowShip("Saruman","Wizard",50,5,8,"Wizard Staff & Dark Sorcery",9)
Sauron = Anti_FellowShip("Sauron","Maiar",500,10,10,"The One Ring",20)
