from entity import MonsterTroll, Character, Dragon
from item import WeaponInstance
import PySimpleGUI as sg
import time
import random

class GameWorld:
    def __init__(self):
        #attributes for gameworld
        #set current game location to start
        self.current_location = "start"
        #create an instance of weapons
        self.weapon_instance = WeaponInstance()
        #call the game items method from weapon instance
        self.weapon_instance.game_items()
        #create an instanace of the character with stat attributes
        self.character = Character(name="Player", entity_class="Barb", race="Human", hit_points=50, damage=1)
        
        #dictonary for game locations
        self.locations = {
            "start": {"description": "You are at the starting point.", "north": "forest", "south": "cave", "east": "castle", "west": "mountain", "image": "images/crossroad.png"},
            "forest": {"description": "You are in a dense forest.", "south": "start", "image": "images/forest.png"},
            "cave": {"description": "You find yourself in a cave.", "north": "start", "image": "images/cave.png"},
            "castle": {"description": "You have found an abandoned castle.", "west": "start", "image": "images/castle.png"},
            "mountain": {"description": "You find yourself in a mountain.", "east": "start", "image": "images/mountain.png"},
        }
        
        #ramdomly select weapons from instanced items. using random.
        self.items = {
            0: random.choice(self.weapon_instance.swords),
            1: random.choice(self.weapon_instance.shields),
            2: random.choice(self.weapon_instance.bows),
            3: random.choice(self.weapon_instance.keys)
        }

        #create monster instances. perhaps this would have been better in the entity class
        self.monsters = [
            MonsterTroll(name="Large Troll", entity_class="Monster", race="Troll", hit_points=6, damage=7),
            MonsterTroll(name="Troll", entity_class="Monster", race="Troll", hit_points=14, damage=5),
            Dragon(name="Gold Dragon", entity_class="Monster", race="Dragon", hit_points=25, damage=10)
        ]
        
    #mthod to get the current locations image
    def get_location_image(self):
        return self.locations[self.current_location].get("image")


    #probably should be in its own class
    def fight(self, character, monster, window):
        #loop if both character and monster have more than 0 hit points
        while character.hit_points > 0 and monster.hit_points > 0:
            
            #the monster takes damage equal to the players current damage
            monster.hit_points -= character.damage
            #print the players attack
            print(f"{character.name} attacks {monster.name} for {character.damage} damage.")
            #allows time to see battle
            time.sleep(.15)
            
            #check if the monster has been slain
            if monster.hit_points <= 0:
                #win condition
                if monster.name == "Gold Dragon":
                    print(f"Congrats!, You have defeated the {monster.name} and beat the game")
                    window.close()
                #print the fight result
                print(f"{monster.name} has been slain")
                return f"you manage to defeat the {monster.name}!"
            
            character.hit_points -= monster.damage
            print(f"{monster.name} attacks {character.name} for {monster.damage} damage")
            time.sleep(.15)
            
             
            if character.hit_points <= 0:
                    sg.popup(f"{character.name} has been killed, game over.")
                    window.close()
                    
        return "The battle is finished."