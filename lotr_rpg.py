from lotr_heroes import Fellowship_Of_The_Ring, Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker
from lotr_enemies import Anti_FellowShip, Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron
import time
import os

heroes = [Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker]
enemies = [Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron]

# for enemy in enemies:
#     print vars(enemy)

# for hero in heroes:
    # print vars(hero)



game_over = False;

while game_over == False:
    print "The fellowship sits in a circle, ready to depart on their mission to destroy The One Ring."
    os.system("say 'The fellowship sits in a circle, ready to depart on their mission to destroy The One Ring.'")
    time.sleep(1)
    print "."
    time.sleep(.3)
    print "."
    time.sleep(.3)
    print "."
    time.sleep(.3)
    os.system("say --voice=tessa 'Choose a character'")
    print "Choose a character"
    print "------------------"
    time.sleep(.1)
    print "1. Aragorn"
    time.sleep(.1)
    print "2. Frodo"
    time.sleep(.1)
    print "3. Samwise_Gamgee"
    time.sleep(.1)
    print "4. Gandalf"
    time.sleep(.1)
    print "5. Gimli"
    time.sleep(.1)
    print "6. Boromir"
    time.sleep(.1)
    print "7. Legolas_Greenleaf"
    time.sleep(.1)
    print "8. Pippin_Took"
    time.sleep(.1)
    print "9. Merry_Brandybuck"
    time.sleep(.1)
    print "10. Faramir"
    time.sleep(.1)
    print "11. Smeagle"
    time.sleep(.1)
    print "12. Drew_Parker"
    time.sleep(.1)
    print "> ",
    input = int(raw_input())

    if input == 1:
        time.sleep(.75)
        print "You have chosen %s" % Aragorn.name
        os.system("say --voice=tessa 'You have selected Aragorn'")
        hero_name = Aragorn.name
        hero_race = Aragorn.race
        hero_health = Aragorn.health
        hero_speed = Aragorn.speed
        hero_strength = Aragorn.strength
        hero_weapon = Aragorn.weapon
        hero_weapon_type = Aragorn.weapon_type
        hero_weapon_power = Aragorn.weapon_power
        hero_physical_resist = Aragorn.physical_resist
        hero_magic_resist = Aragorn.magic_resist
    elif input == 2:
        time.sleep(.75)
        print "You have chosen %s" % Frodo.name
        os.system("say --voice=tessa 'You have selected Frodo'")
        hero_name = Frodo.name
        hero_race = Frodo.race
        hero_health = Frodo.health
        hero_speed = Frodo.speed
        hero_strength = Frodo.strength
        hero_weapon = Frodo.weapon
        hero_weapon_type = Frodo.weapon_type
        hero_weapon_power = Frodo.weapon_power
        hero_physical_resist = Frodo.physical_resist
        hero_magic_resist = Frodo.magic_resist
    elif input == 3:
        time.sleep(.75)
        print "You have chosen %s" % Samwise_Gamgee.name
        os.system("say --voice=tessa 'You have selected Samwise Gamgee'")
        hero_name = Samwise_Gamgee.name
        hero_race = Samwise_Gamgee.race
        hero_health = Samwise_Gamgee.health
        hero_speed = Samwise_Gamgee.speed
        hero_strength = Samwise_Gamgee.strength
        hero_weapon = Samwise_Gamgee.weapon
        hero_weapon_type = Samwise_Gamgee.weapon_type
        hero_weapon_power = Samwise_Gamgee.weapon_power
        hero_physical_resist = Samwise_Gamgee.physical_resist
        hero_magic_resist = Samwise_Gamgee.magic_resist
    elif input == 4:
        time.sleep(.75)
        print "You have chosen %s" % Gandalf.name
        os.system("say --voice=tessa 'You have selected Gandalf'")
        hero_name = Gandalf.name
        hero_race = Gandalf.race
        hero_health = Gandalf.health
        hero_speed = Gandalf.speed
        hero_strength = Gandalf.strength
        hero_weapon = Gandalf.weapon
        hero_weapon_type = Gandalf.weapon_type
        hero_weapon_power = Gandalf.weapon_power
        hero_physical_resist = Gandalf.physical_resist
        hero_magic_resist = Gandalf.magic_resist
    elif input == 5:
        time.sleep(.75)
        print "You have chosen %s" % Gimli.name
        os.system("say --voice=tessa 'You have selected Gimli'")
        hero_name = Gimli.name
        hero_race = Gimli.race
        hero_health = Gimli.health
        hero_speed = Gimli.speed
        hero_strength = Gimli.strength
        hero_weapon = Gimli.weapon
        hero_weapon_type = Gimli.weapon_type
        hero_weapon_power = Gimli.weapon_power
        hero_physical_resist = Gimli.physical_resist
        hero_magic_resist = Gimli.magic_resist
    elif input == 6:
        time.sleep(.75)
        print "You have chosen %s" % Boromir.name
        os.system("say --voice=tessa 'You have selected Boromir'")
        hero_name = Boromir.name
        hero_race = Boromir.race
        hero_health = Boromir.health
        hero_speed = Boromir.speed
        hero_strength = Boromir.strength
        hero_weapon = Boromir.weapon
        hero_weapon_type = Boromir.weapon_type
        hero_weapon_power = Boromir.weapon_power
        hero_physical_resist = Boromir.physical_resist
        hero_magic_resist = Boromir.magic_resist
    elif input == 7:
        time.sleep(.75)
        print "You have chosen %s" % Legolas_Greenleaf.name
        os.system("say --voice=tessa 'You have selected Legolas'")
        hero_name = Legolas_Greenleaf.name
        hero_race = Legolas_Greenleaf.race
        hero_health = Legolas_Greenleaf.health
        hero_speed = Legolas_Greenleaf.speed
        hero_strength = Legolas_Greenleaf.strength
        hero_weapon = Legolas_Greenleaf.weapon
        hero_weapon_type = Legolas_Greenleaf.weapon_type
        hero_weapon_power = Legolas_Greenleaf.weapon_power
        hero_physical_resist = Legolas_Greenleaf.physical_resist
        hero_magic_resist = Legolas_Greenleaf.magic_resist
    elif input == 8:
        time.sleep(.75)
        print "You have chosen %s" % Pippin_Took.name
        os.system("say --voice=tessa 'You have selected Pippin Took'")
        hero_name = Pippin_Took.name
        hero_race = Pippin_Took.race
        hero_health = Pippin_Took.health
        hero_speed = Pippin_Took.speed
        hero_strength = Pippin_Took.strength
        hero_weapon = Pippin_Took.weapon
        hero_weapon_type = Pippin_Took.weapon_type
        hero_weapon_power = Pippin_Took.weapon_power
        hero_physical_resist = Pippin_Took.physical_resist
        hero_magic_resist = Pippin_Took.magic_resist
    elif input == 9:
        time.sleep(.75)
        print "You have chosen %s" % Merry_Brandybuck.name
        os.system("say --voice=tessa 'You have selected Merry Brandybuck'")
        hero_name = Merry_Brandybuck.name
        hero_race = Merry_Brandybuck.race
        hero_health = Merry_Brandybuck.health
        hero_speed = Merry_Brandybuck.speed
        hero_strength = Merry_Brandybuck.strength
        hero_weapon = Merry_Brandybuck.weapon
        hero_weapon_type = Merry_Brandybuck.weapon_type
        hero_weapon_power = Merry_Brandybuck.weapon_power
        hero_physical_resist = Merry_Brandybuck.physical_resist
        hero_magic_resist = Merry_Brandybuck.magic_resist
    elif input == 10:
        time.sleep(.75)
        print "You have chosen %s" % Faramir.name
        os.system("say --voice=tessa 'You have selected Faramir'")
        hero_name = Faramir.name
        hero_race = Faramir.race
        hero_health = Faramir.health
        hero_speed = Faramir.speed
        hero_strength = Faramir.strength
        hero_weapon = Faramir.weapon
        hero_weapon_type = Faramir.weapon_type
        hero_weapon_power = Faramir.weapon_power
        hero_physical_resist = Faramir.physical_resist
        hero_magic_resist = Faramir.magic_resist
    elif input == 11:
        time.sleep(.75)
        print "You have chosen %s" % Smeagle.name
        os.system("say --voice=tessa 'You have selected Smeagle'")
        hero_name = Smeagle.name
        hero_race = Smeagle.race
        hero_health = Smeagle.health
        hero_speed = Smeagle.speed
        hero_strength = Smeagle.strength
        hero_weapon = Smeagle.weapon
        hero_weapon_type = Smeagle.weapon_type
        hero_weapon_power = Smeagle.weapon_power
        hero_physical_resist = Smeagle.physical_resist
        hero_magic_resist = Smeagle.magic_resist
    elif input == 12:
        time.sleep(.75)
        print "You have chosen %s" % Drew_Parker.name
        os.system("say --voice=tessa 'You have selected The Man, The Myth, The Legend... Drew Parker'")
        hero_name = Drew_Parker.name
        hero_race = Drew_Parker.race
        hero_health = Drew_Parker.health
        hero_speed = Drew_Parker.speed
        hero_strength = Drew_Parker.strength
        hero_weapon = Drew_Parker.weapon
        hero_weapon_type = Drew_Parker.weapon_type
        hero_weapon_power = Drew_Parker.weapon_power
        hero_physical_resist = Drew_Parker.physical_resist
        hero_magic_resist = Drew_Parker.magic_resist
    else:
        print "You suck"
        os.system("say 'You Suck'")
        game_over = True;
    if game_over == True:
        print "You have lost"
        os.system("say 'Game Over'")
    else:
        print "1: Continue?"
        print "2: Quit"
        os.system("say --voice=tessa 'Continue?'")

        input = int(raw_input())
        if input == 1:
            print "Good luck"
            os.system("say --voice=tessa 'Good Luck'")
            time.sleep(1.5)
        elif input == 2:
            print "Too bad, you're stuck in the game"
            os.system("say 'Too bad, you are stuck in the game'")
            time.sleep(1.5)
        else:
            print "continue anyway"
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
        os.system("say -r 20 'OH'")
        os.system("say -r 20 'MY'")
        os.system("say --voice=tessa 'ZEESH'")
        time.sleep(2)
        print "%s's attributes are:" % (hero_name)
        os.system("say --voice=tessa 'Your heroes attributes are as follows'")
        print "------------------"
        time.sleep(.3)
        print "Name: %s" % (hero_name)
        time.sleep(.3)
        print "Race: %s" % (hero_race)
        time.sleep(.3)
        print "Health: %s" % (hero_health)
        time.sleep(.3)
        print "Speed: %s" % (hero_speed)
        time.sleep(.3)
        print "Strength: %s" % (hero_strength)
        time.sleep(.3)
        print "Weapon: %s" % (hero_weapon)
        time.sleep(.3)
        print "Weapon Type: %s" % (hero_weapon_type)
        time.sleep(.3)
        print "Weapon Power: %s" % (hero_weapon_power)
        time.sleep(.3)
        print "Physical Resist: %s" % (hero_physical_resist)
        time.sleep(.3)
        print "Magic Resist: %s" % (hero_magic_resist)
        time.sleep(.5)
        print "------------------"
        time.sleep(2)
        print "Time to set off on your journey"
        os.system("say 'Time to set off on your journey'")
        time.sleep(.5)
        print "."
        time.sleep(.3)
        print "."
        time.sleep(.3)
        print "."
        time.sleep(.3)
        print "lalalalalal time passes"
        os.system("say 'Lalalalalalala... Time passes'")
        time.sleep(1)
        print "."
        time.sleep(.3)
        print "."
        time.sleep(.3)
        print "."
        time.sleep(.3)
        print "!!"
        os.system("say 'OH MY GOD WATCH OUT'")
        time.sleep(1.5)
        os.system("say -r 50 'DEAR GOD'")
        time.sleep(.7)
        print "You have encountered a giant Cave Troll while travelling through the Mines of Moria!"
        os.system("say 'You have encountered a Cave Troll while travelling through the Mines of Moria!'")
        time.sleep(2)
        print "Will you fight?"
        os.system("say 'Will you fight? Or are you a coward like Michael Irby'")
        time.sleep(1)
        print "1: Fight"
        print "2: Michael Irby"
        input = int(raw_input())
        if input == 1:
            print "The Cave_Troll lunges at you swiftly"
            os.system("say 'The Cave_Troll lunges at you swiftly'")
            time.sleep(2)
            if Cave_Troll.speed < hero_speed:
                enemy_health = Cave_Troll.health - hero_strength;
                hero_health = hero_health - (.5 * Cave_Troll.strength)
                print "You quickly maneuver around a pillar and counter-attack!"
                os.system("say 'You quickly maneuver around a pillar and counter-attack!'")
                time.sleep(.5)
                print "You trade blows with the cave troll"
                os.system("say 'You trade blows with the cave troll'")
                time.sleep(.5)
                print "The Cave_Troll named %s has taken %d damage thanks to %s's speed!" % (Cave_Troll.name, hero_strength, hero_name)
                os.system("say 'The Cave Troll named Pateesa has taken damage thanks to your speed'")
                time.sleep(2)
                print "The Cave_Troll now has %d health left." % (enemy_health)

                print "%s now has %d health left." % (hero_name, hero_health)
                if enemy_health <= 0:
                    print "%s has defeated the Cave Troll named %s" % (hero_name, Cave_Troll.name)
                    os.system("say 'You have defeated the Cave Troll named Pateesa'")
                    time.sleep(3);
                    game_over = True
                    if game_over == True:
                        print "."
                        time.sleep(.3)
                        print "."
                        time.sleep(.3)
                        print "."
                        time.sleep(.3)
                        print "Still working on the rest of the game. Thanks for playing"
                        os.system("say 'More coming soon. Thanks for playing'")
            else:
                hero_health = hero_health - Cave_Troll.strength
                enemy_health = Cave_Troll.health - (.5 * hero_strength)
                print "You trade blows with the cave troll"
                time.sleep(1)
                print "You took %d damage because %s is faster than %s" % (Cave_Troll.strength, Cave_Troll.name, hero_name)
                print "The Cave_Troll named %s has taken %d damage" % (Cave_Troll.name, (.5 * hero_strength))
                time.sleep(2)
                print "You now have %d health left" % (hero_health)
            print
            game_over = True;
            if game_over == True:
                print "Keep making the game, Sean"
        elif input == 2:
            print "Dammit. You are just like the Irbinator"
            os.system("say 'Dammit... You are just like Irby. Game Over'")
            time.sleep(1.5)
            os.system("say 'For the purpose of the demo, we will continue the game as if you are not a coward'")
            time.sleep(1.5)
            print "The Cave_Troll lunges at you swiftly"
            os.system("say 'The Cave_Troll lunges at you swiftly'")
            time.sleep(2)
            if Cave_Troll.speed < hero_speed:
                enemy_health = Cave_Troll.health - hero_strength;
                hero_health = hero_health - (.5 * Cave_Troll.strength)
                print "You quickly maneuver around a pillar and counter-attack!"
                os.system("say 'You quickly maneuver around a pillar and counter-attack!'")
                time.sleep(.5)
                print "You trade blows with the cave troll"
                os.system("say 'You trade blows with the cave troll'")
                time.sleep(.5)
                print "The Cave_Troll named %s has taken %d damage thanks to %s's speed!" % (Cave_Troll.name, hero_strength, hero_name)
                os.system("say 'The Cave Troll named Pateesa has taken damage thanks to your speed'")
                time.sleep(2)
                print "The Cave_Troll now has %d health left." % (enemy_health)

                print "%s now has %d health left." % (hero_name, hero_health)
                if enemy_health <= 0:
                    print "%s has defeated the Cave Troll named %s" % (hero_name, Cave_Troll.name)
                    os.system("say 'You have defeated the Cave Troll named Pateesa'")
                    time.sleep(2);
                    game_over = True
                    if game_over == True:
                        print "."
                        time.sleep(.3)
                        print "."
                        time.sleep(.3)
                        print "."
                        time.sleep(.3)
                        print "Still working on the rest of the game. Thanks for playing"
                        os.system("say 'More coming soon. Thanks for playing'")
                else:
                    print "The troll named %s is on his last legs" % (Cave_Troll.name)
                    os.system("say 'The troll named Pateesa is on his last legs.'")
                    time.sleep(.3)
                    print "Keep fighting?"
                    os.system("say 'Keep fighting?'")
                    time.sleep(.3)
                    print "1: Fight"
                    print "2: Flee"
                    input = int(raw_input())
                    # yes
                    if input == 1:
                        if Cave_Troll.speed < hero_speed:
                            enemy_health = enemy_health - hero_strength;
                            hero_health = hero_health - (.5 * Cave_Troll.strength)
                            print "You trade blows with the cave troll again"
                            os.system("say 'You trade blows with the cave troll again.'")
                            time.sleep(.5)
                            print "The Cave_Troll named %s has taken %d damage thanks to %s's speed!" % (Cave_Troll.name, hero_strength, hero_name)
                            os.system("say 'The Cave Troll named Pateesa has taken damage thanks to your speed'")
                            time.sleep(2)
                            print "The Cave_Troll now has %d health left." % (enemy_health)
                            if enemy_health <= 0:
                                print "%s has defeated the Cave Troll named %s" % (hero_name, Cave_Troll.name)
                                os.system("say 'You have defeated the Cave Troll named Pateesa'")
                                time.sleep(2);
                                game_over = True
                                if game_over == True:
                                    print "."
                                    time.sleep(.3)
                                    print "."
                                    time.sleep(.3)
                                    print "."
                                    time.sleep(.3)
                                    print "Still working on the rest of the game. Thanks for playing"
                                    os.system("say 'More coming soon. Thanks for playing'")
                    elif input == 2:
                        print "The Cave troll Blocks the exit. You cannot escape"
                        os.system("Why are you so cowardly? Either way, the Cave Troll blocked the exit. You cannot escape")
                        time.sleep(2)
                        if Cave_Troll.speed < hero_speed:
                            enemy_health = enemy_health - hero_strength;
                            hero_health = hero_health - (.5 * Cave_Troll.strength)
                            print "You trade blows with the cave troll again"
                            os.system("say 'You trade blows with the cave troll once more.'")
                            time.sleep(.5)
                            print "The Cave_Troll named %s has taken %d damage thanks to %s's speed!" % (Cave_Troll.name, hero_strength, hero_name)
                            os.system("say 'The Cave Troll named Pateesa has taken damage thanks to your speed'")
                            time.sleep(2)
                            print "The Cave_Troll now has %d health left." % (enemy_health)
                            if enemy_health <= 0:
                                print "%s has defeated the Cave Troll named %s" % (hero_name, Cave_Troll.name)
                                os.system("say 'You have defeated the Cave Troll named Pateesa'")
                                time.sleep(2);
                                game_over = True
                                if game_over == True:
                                    print "."
                                    time.sleep(.3)
                                    print "."
                                    time.sleep(.3)
                                    print "."
                                    time.sleep(.3)
                                    print "Still working on the rest of the game. Thanks for playing"
                                    os.system("say 'More coming soon. Thanks for playing'")


            else:
                hero_health = hero_health - Cave_Troll.strength
                enemy_health = Cave_Troll.health - (.5 * hero_strength)
                print "You trade blows with the cave troll"
                time.sleep(1)
                print "You took %d damage because %s is faster than %s" % (Cave_Troll.strength, Cave_Troll.name, hero_name)
                print "The Cave_Troll named %s has taken %d damage" % (Cave_Troll.name, (.5 * hero_strength))
                time.sleep(2)
                print "You now have %d health left" % (hero_health)
            print
            game_over = True;
            if game_over == True:
                print "Keep making the game, Sean"
