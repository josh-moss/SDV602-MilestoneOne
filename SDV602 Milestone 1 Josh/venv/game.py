import PySimpleGUI as sg 
from world import GameWorld
import random

class CommandParser:
    def __init__(self, game_world, window):
        #instance gameworld
        self.game_world = game_world
        self.window = window
        
    def parse_command(self, command):
        #check if command is an valid option
        if command in ["north", "south", "east", "west"]:
            #call the move method to change location
            return self.move(command)
        
        elif command == "inventory":
            #display the instanced characters inventory if the command is input
            return self.game_world.character.check_inventory()
        
        elif command == "equip":
            #create a list comprehension of all item names in the character's inventory
            item_names = [item.item_name for item in self.game_world.character.inventory]
            
            if item_names:
                #prompt the player to enter the name of the item they wish to equip
                item_to_equip = sg.popup_get_text("type the name of the item to equip", title="Equip item")
                
                #check if the player clicked cancel or closed the popup
                if not item_to_equip:
                    return "no item was selected."
                
                #check if the entered item name is in the inventory
                if item_to_equip in item_names:
                    return self.game_world.character.equip_item(item_to_equip)
                
                else:
                    return "no item found by that name."
                
            else:
                return "inventory is empty."
            
        elif command == "unequip":
            return self.game_world.character.unequip_item()
        
        elif command == "quit":
            return "quit"
        
        else:
            return "invalid Command."
        
        
    def move(self, direction):
        #check if the location is vaid
        if direction not in ["north", "south", "east", "west"]:
            return "invalid direction."
        
        
        #change current location if the location is valid and display the description of the new location
        if direction in self.game_world.locations[self.game_world.current_location]:
            self.game_world.current_location = self.game_world.locations[self.game_world.current_location][direction]
            location_description = self.game_world.locations[self.game_world.current_location]["description"]
            
            print(f"{location_description}")
            
            
            location_image = self.game_world.get_location_image()
            #update the current locations image in the window
            if location_image:
                self.window["-IMG-"].update(filename=location_image)
                
            #random encounters for each location, this is either an item or monster
            if random.choice([True, False]):
                
                #randomly selects items from the random item list in the gameworld instance 
                item = self.game_world.items[random.randint(0, len(self.game_world.items) -1)]
                
                #display the randomly selected item
                item_encounter = f"you found an item {item.item_name}"
                
                #prompt the player with an option to take or leave the encountered item
                pickup = sg.popup_yes_no(f"{item_encounter}\ndo you want to pick it up?", title="Adventure game")
                
                if pickup == 'Yes':
                    #append the random item to the player's inventory
                    self.game_world.character.add_to_inventory(item)
                    return f"{item_encounter} has been added to your inventory."
                
                else:
                    return "You leave the item behind."
                
            else:
                #randomly selects monsters from the instantiated monsters list in gameworld
                monster = self.game_world.monsters[random.randint(0, len(self.game_world.monsters) -1)]
                
                monster_encounter = f"you encounter a {monster.name}"
                
                fight = sg.popup_yes_no(f"{monster_encounter}\nDo you want to fight the {monster.name}?", title="Adventure game")
                
                if fight == 'Yes':
                    #call the fight method in gameworld
                    fight_result = self.game_world.fight(self.game_world.character, monster, self.window)
                    if fight_result == "run_away":
                        print("you ran away")
                    return fight_result
                
                else:
                    return "you escape the encounter."
                
        else:
            return "You can't go that way."


#perhaps this should be a class?
def main():
    game_world = GameWorld()
    
    #window layout
    sg.theme("Dark Blue 14")
    layout = [[sg.Image(size=(440,440), key="-IMG-")],
              [sg.Output(size=(60, 5))],
              [sg.Text("Available Commands: North, South, East, West, Inventory, Equip, Unequip, Quit")],
              [sg.Text("Enter a command:"), sg.Input(key='-IN-', focus=True)],
              [sg.Button('Submit', bind_return_key=True), sg.Button('Quit', bind_return_key=True)]]
    
    #init window
    window = sg.Window('Adventure Game', layout, finalize=True)
    parser = CommandParser(game_world, window)
    window["-IMG-"].update(filename=game_world.get_location_image())
    sg.popup("You wake up and find yourself at a crossroad. What will you do next?", title="Adventure game")
    
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        
        if event == 'Submit':
            command = values['-IN-'].lower()
            result = parser.parse_command(command)

            # exit loop if quit is called
            if result == "quit":
                break

            print(result)
            
            
    #window is closed once the loop is broken        
    window.close()

if __name__ == "__main__":
    main()