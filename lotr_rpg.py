from lotr_heroes import Fellowship_Of_The_Ring, Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker
from lotr_enemies import Anti_FellowShip, Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron
import time

heroes = [Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker]
enemies = [Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron]

# for enemy in enemies:
#     print vars(enemy)

# for hero in heroes:
    # print vars(hero)



game_over = False;

while game_over == False:
    print "The fellowship sits in a circle, ready to depart on their mission to destroy The One Ring."
    print "Choose a character"
    print "------------------"
    print "1. Aragorn"
    print "2. Frodo"
    print "3. Samwise_Gamgee"
    print "4. Gandalf"
    print "5. Gimli"
    print "6. Boromir"
    print "7. Legolas_Greenleaf"
    print "8. Pippin_Took"
    print "9. Merry_Brandybuck"
    print "10. Faramir"
    print "11. Smeagle"
    print "12. Drew_Parker"
    print "> ",
    input = int(raw_input())

    if input == 1:
        time.sleep(.75)
        print "You have chosen %s" % Aragorn.name
        hero_name = Aragorn.name
        hero_race = Aragorn.race
        hero_health = Aragorn.health
        hero_speed = Aragorn.speed
        hero_strength = Aragorn.strength
        hero_weapon = Aragorn.weapon
        hero_weapon_power = Aragorn.weapon_power
    elif input == 2:
        time.sleep(.75)
        print "You have chosen %s" % Frodo.name
        hero_name = Frodo.name
        hero_race = Frodo.race
        hero_health = Frodo.health
        hero_speed = Frodo.speed
        hero_strength = Frodo.strength
        hero_weapon = Frodo.weapon
        hero_weapon_power = Frodo.weapon_power
    elif input == 3:
        time.sleep(.75)
        print "You have chosen %s" % Samwise_Gamgee.name
        hero_name = Samwise_Gamgee.name
        hero_race = Samwise_Gamgee.race
        hero_health = Samwise_Gamgee.health
        hero_speed = Samwise_Gamgee.speed
        hero_strength = Samwise_Gamgee.strength
        hero_weapon = Samwise_Gamgee.weapon
        hero_weapon_power = Samwise_Gamgee.weapon_power
    elif input == 4:
        time.sleep(.75)
        print "You have chosen %s" % Gandalf.name
        hero_name = Gandalf.name
        hero_race = Gandalf.race
        hero_health = Gandalf.health
        hero_speed = Gandalf.speed
        hero_strength = Gandalf.strength
        hero_weapon = Gandalf.weapon
        hero_weapon_power = Gandalf.weapon_power
    elif input == 5:
        time.sleep(1.5)
        print "You have chosen %s" % Gimli.name
        hero_name = Gimli.name
        hero_race = Gimli.race
        hero_health = Gimli.health
        hero_speed = Gimli.speed
        hero_strength = Gimli.strength
        hero_weapon = Gimli.weapon
        hero_weapon_power = Gimli.weapon_power
    elif input == 6:
        time.sleep(1.5)
        print "You have chosen %s" % Boromir.name
        hero_name = Boromir.name
        hero_race = Boromir.race
        hero_health = Boromir.health
        hero_speed = Boromir.speed
        hero_strength = Boromir.strength
        hero_weapon = Boromir.weapon
        hero_weapon_power = Boromir.weapon_power
    elif input == 7:
        time.sleep(1.5)
        print "You have chosen %s" % Legolas_Greenleaf.name
        hero_name = Legolas_Greenleaf.name
        hero_race = Legolas_Greenleaf.race
        hero_health = Legolas_Greenleaf.health
        hero_speed = Legolas_Greenleaf.speed
        hero_strength = Legolas_Greenleaf.strength
        hero_weapon = Legolas_Greenleaf.weapon
        hero_weapon_power = Legolas_Greenleaf.weapon_power
    elif input == 8:
        time.sleep(1.5)
        print "You have chosen %s" % Pippin_Took.name
        hero_name = Pippin_Took.name
        hero_race = Pippin_Took.race
        hero_health = Pippin_Took.health
        hero_speed = Pippin_Took.speed
        hero_strength = Pippin_Took.strength
        hero_weapon = Pippin_Took.weapon
        hero_weapon_power = Pippin_Took.weapon_power
    elif input == 9:
        time.sleep(1.5)
        print "You have chosen %s" % Merry_Brandybuck.name
        hero_name = Merry_Brandybuck.name
        hero_race = Merry_Brandybuck.race
        hero_health = Merry_Brandybuck.health
        hero_speed = Merry_Brandybuck.speed
        hero_strength = Merry_Brandybuck.strength
        hero_weapon = Merry_Brandybuck.weapon
        hero_weapon_power = Merry_Brandybuck.weapon_power
    elif input == 10:
        time.sleep(1.5)
        print "You have chosen %s" % Faramir.name
        hero_name = Faramir.name
        hero_race = Faramir.race
        hero_health = Faramir.health
        hero_speed = Faramir.speed
        hero_strength = Faramir.strength
        hero_weapon = Faramir.weapon
        hero_weapon_power = Faramir.weapon_power
    elif input == 11:
        time.sleep(1.5)
        print "You have chosen %s" % Smeagle.name
        hero_name = Smeagle.name
        hero_race = Smeagle.race
        hero_health = Smeagle.health
        hero_speed = Smeagle.speed
        hero_strength = Smeagle.strength
        hero_weapon = Smeagle.weapon
        hero_weapon_power = Smeagle.weapon_power
    elif input == 12:
        time.sleep(1.5)
        print "You have chosen %s" % Drew_Parker.name
        hero_name = Drew_Parker.name
        hero_race = Drew_Parker.race
        hero_health = Drew_Parker.health
        hero_speed = Drew_Parker.speed
        hero_strength = Drew_Parker.strength
        hero_weapon = Drew_Parker.weapon
        hero_weapon_power = Drew_Parker.weapon_power
    else:
        print "You suck"
        game_over = True;
    if game_over == True:
        print "You have lost"
    else:
        print "1: Continue?"
        print "2: Quit"

        input = int(raw_input())
        if input == 1:
            print "Good luck"
        else:
            print "Too bad you're stuck in the game"
        print
        print "         __                                     __"
        time.sleep(.1)
        print "  ____  / /_     ____ ___  __  __   ____  _____/ /_"
        time.sleep(.1)
        print " / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \ "
        time.sleep(.1)
        print "/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /"
        time.sleep(.1)
        print "\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/"
        time.sleep(.1)
        print "                           /_/"
        time.sleep(1)
        print "These are %s's attributes" % (hero_name)
        print "------------------"
        time.sleep(.2)
        print "Name: %s" % (hero_name)
        time.sleep(.2)
        print "Race: %s" % (hero_race)
        time.sleep(.2)
        print "Health: %s" % (hero_health)
        time.sleep(.2)
        print "Speed: %s" % (hero_speed)
        time.sleep(.2)
        print "Strength: %s" % (hero_strength)
        time.sleep(.2)
        print "Weapon: %s" % (hero_weapon)
        time.sleep(.2)
        print "Weapon Power: %s" % (hero_weapon_power)
        time.sleep(.5)
        print "------------------"
        time.sleep(2)
        print "Time to set off on your journey"
        time.sleep(1)
        print "lalalalalal time passes"
        time.sleep(2)
        print "You have encountered a Cave Troll while travelling through the Mines of Moria!"
        time.sleep(2)
        print "Will you fight?"
        time.sleep(1)
        print "1: Fight"
        print "2: I'm a coward"
        input = int(raw_input())
        if input == 1:
            print "%s lunges at you before you can even move" % (Cave_Troll.name)
            time.sleep(2)
            if Cave_Troll.speed < hero_speed:
                enemy_health = Cave_Troll.health - hero_strength;
                print "The Cave_Troll named %s has taken %d damage thanks to %s's speed!" % (Cave_Troll.name, hero_strength, hero_name)
                time.sleep(2)
                print "The Cave_Troll now has %d health left" % (enemy_health)
            else:
                hero_health = hero_health - Cave_Troll.strength
                print "You took %d damage because %s is faster than %s" % (Cave_Troll.strength, Cave_Troll.name, hero_name)
                time.sleep(2)
                print "You now have %d health left" % (hero_health)
            game_over = True;
            if game_over == True:
                print "Keep making the game, Sean"
        else:
            game_over = True;
            if game_over == True:
                print "Keep making the game, Sean"
