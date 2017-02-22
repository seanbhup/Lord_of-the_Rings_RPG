from lotr_heroes import Fellowship_Of_The_Ring, Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker
from lotr_enemies import Anti_FellowShip, Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron
import time

heroes = [Aragorn, Gimli, Frodo, Samwise_Gamgee, Gandalf, Boromir, Faramir, Merry_Brandybuck, Pippin_Took, Legolas_Greenleaf, Smeagle, Drew_Parker]
enemies = [Orc_Grunt, Cave_Troll, Lurtz, Nazgul, Balrog, Gollum, Saruman, Sauron]

# for enemy in enemies:
    # print vars(enemy)

# for hero in heroes:
    # print vars(hero)


print "The fellowship sits in a circle, ready to depart to destroy The One Ring."
print "Choose a character"
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
elif input == 2:
    time.sleep(.75)
    print "You have chosen %s" % Frodo.name
elif input == 3:
    time.sleep(.75)
    print "You have chosen %s" % Samwise_Gamgee.name
elif input == 4:
    time.sleep(.75)
    print "You have chosen %s" % Gandalf.name
elif input == 5:
    time.sleep(1.5)
    print "You have chosen %s" % Gimli.name
elif input == 6:
    time.sleep(1.5)
    print "You have chosen %s" % Boromir.name
elif input == 7:
    time.sleep(1.5)
    print "You have chosen %s" % Legolas_Greenleaf.name
elif input == 8:
    time.sleep(1.5)
    print "You have chosen %s" % Pippin_Took.name
elif input == 9:
    time.sleep(1.5)
    print "You have chosen %s" % Merry_Brandybuck.name
elif input == 10:
    time.sleep(1.5)
    print "You have chosen %s" % Faramir.name
elif input == 11:
    time.sleep(1.5)
    print "You have chosen %s" % Smeagle.name
elif input == 12:
    time.sleep(1.5)
    print "You have chosen %s" % Drew_Parker.name
else:
    print "You suck"
print "Continue?"

input = str(raw_input())
if input == "yes" or "Yes" or "YES" or "y" or "Y" or "yES" or "yeS" or "yEs":
    print "Good luck"
else:
    print "Too bad you're stuck in the game"



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
time.sleep(.1)
