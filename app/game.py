import csv
from csv import writer

headers = ["decision"]

csvfile = "log.csv"
f = open(csvfile, "w+")
f.close()

class MyCharacter:
    def __init__(self, title, ability):
        self.title = title
        self.ability = ability

character_1 = MyCharacter("BeanMan", "Bean Toss")
character_2 = MyCharacter("EggMan", "Egg Toss")
character_3 = MyCharacter("SaladBoy", "Salad Toss")

def fourth_decision(surrender_fight, char):
    csvfile = open('log.csv', 'r')
    reader = csv.DictReader(csvfile, "t")
    all_lines = list(reader)
    number_of_lines = len(all_lines) + 1
    if surrender_fight.lower() == "surrender":
        data = ["surrender"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    the soldiers capture you and take you to a secret lab.                                                  *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*  you become a permanent test subject for the united states government because of your {char.title} powers.*")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    GAME OVER.                                                                                              *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*                         you took {number_of_lines} turns to lose the game!                                *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
    elif surrender_fight.lower() == "fight":
        data = ["fight"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    using all the skills you've acquired so far..                                                           *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*   you beat those soldiers up very easily using the ultimate power of {char.ability}                       *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    one of the soliders is very beautiful and friendly and you guys fall in love                            *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you live happily ever after. aww                                                                        *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*                         you took {number_of_lines} turns to finish the game!                              *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
    else:
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    invalid                                                                                                 *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        surrender_fight = input("surrender/fight?")
        fourth_decision(surrender_fight, char)


def third_decision(help_hijack, char):
    if help_hijack.lower() == "help":
        data = ["help"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*    the careful gentle astronauts have mercy on your weary {char.title} soul.                              *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    they put you out of your misery using the cannons built into the international space station. try again *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        intro_point(char)
    elif help_hijack.lower() == "hijack":
        data = ["hijack"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you manage to take control of the spaceship and dump the silly astronauts into the void of space        *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you know how to drive a spaceship for some reason. you land on earth safely.                            *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    once you land, there are many angry soldiers on the ground.                                             *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*    do you surrender or do you fight using {char.ability}?                                                 *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        surrender_fight = input("surrender/fight?")
        fourth_decision(surrender_fight, char)
    else:
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    invalid                                                                                                 *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        help_hijack = input("help/hijack")
        third_decision(help_hijack, char)

def second_decision(drill_motor, char):
    if drill_motor.lower() == 'drill':
        data = ["drill"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you are now at the center of the earth. good job. you rest here for eterity. try again.                 *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        intro_point(char)
    elif drill_motor.lower() == "motor":
        data = ["motor"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you shoot out of the volcano! but your motor is so strong that you end up in space! golly gee           *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    luckily you spy the international space station nearby. you can either:                                 *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    try to get them to help you? or hijack the ISS like a monster?                                          *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        help_hijack = input("help/hijack")
        third_decision(help_hijack, char)
    else:
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    invalid. help or hijack?                                                                                *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        help_hijack = input("help/hijack")
        third_decision(help_hijack, char)


def first_decision(swim_climb, char):
    if swim_climb.lower() == "swim":
        data = ["swim"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    wow you have developed super powers! you make it through the lava without being burned                  *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you are now at the bottom of the volcano.                                                               *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    even though you are lava-proof, you do not have the power to hold your breath for very long  .          *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    you feel your lungs giving out. you can either:                                                         *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    undergo metamorphosis and grow a horn on your head to drill through bedrock?  OR                        *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print("*    undergo metamorphosis to grow a motor at the base of your sacral spine and fly up out of the volcano    *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        drill_motor = input("drill/motor?")
        second_decision(drill_motor, char)
    elif swim_climb.lower() == "climb":
        data = ["climb"]
        with open('log.csv', 'a') as csvfile:
            writer_object=writer(csvfile)
            writer_object.writerow(data)
            csvfile.close()
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*sadly you are not half monkey. You are merely {char.title}. You land back on the volcano floor like a loser.*")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        intro_point(char)
    else: 
        print("**************************************************************************************************************")
        print("*                                                                                                            *")
        print(f"*    hey pick one of the 2 options {char.title}                                                             *")
        print("*                                                                                                            *")
        print("**************************************************************************************************************")
        swim_climb = input("    swim or climb?  ")
        first_decision(swim_climb, char)

def intro_point(char):
    print(char.title)
    print("**************************************************************************************************************")
    print("*                                                                                                            *")
    print(f"*    welcome {char.title}. You have landed in an active volcano after jumping out of a plane.              *")
    print("*                                                                                                            *") 
    print("**************************************************************************************************************")
    print("*                                                                                                            *")
    print("*    But the thing is, you hit your head on the rim of the volcano so you don't remember anything!           *")
    print("*                                                                                                            *")
    print("**************************************************************************************************************")
    print("*                                                                                                            *")
    print("*    you have two options now.                                                                               *")
    print("*                                                                                                            *") 
    print("**************************************************************************************************************")
    print("*                                                                                                            *")
    print("*    Hope that you've developed latent superpowers and swim through the lava? Or try to climb your way out?  *")
    print("*                                                                                                            *")
    print("**************************************************************************************************************")
    swim_climb = input("    swim or climb?  ")
    first_decision(swim_climb, char)

def character_selection():
    char = character_1
    character_select = int(input("would you rather be BeanMan, EggMan, or SaladBoy? Enter 1, 2, or 3:   "))
    if character_select == 1:
        char =  character_1
    elif character_select == 2:
        char = character_2
    elif character_select == 3:
        char = character_3
    else:
        character_selection()
    intro_point(char)

character_selection()
    