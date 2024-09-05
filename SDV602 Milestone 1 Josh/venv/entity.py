import PySimpleGUI as sg

#entity super class for inheritinng common attributes and methods shaared between objects
class Entity:
    def __init__(self, name="", entity_class="", race=""):
        self.name = name
        self.entity_class = entity_class
        self.race = race
    
    
    def attack(self):
        return f"{self.name} Attacks For {self.damage} Damage"
    
    
#the player character class holds attributes and methods that belong to the player, e.g inventory, equip, etc
class Character(Entity):
    def __init__(self, name="", entity_class="", race="", inventory=None, hit_points=0, damage=0):
        super().__init__(name, entity_class, race)
        self.hit_points = hit_points
        self.damage = damage
        self.attack()
        
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    #loop though each item in players inventory, if the item exists then change the players damage to the items damage
    def equip_item(self, item_name):
        for item in self.inventory:
            if item.item_name == item_name:
                self.damage = item.item_damage
                return f"{item.item_name} equipped, you now deal {self.damage} damage."
        return "Item not found in inventory."
    
    #removes the equip item, resets damage to 1
    def unequip_item(self):
        self.damage = 1
        return f"Item unequipped. you now deal {self.damage} damage"
        
    # when this method is called the item is appended to the characters inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)
        
        
    def check_inventory(self):
        #joins each item in inventory and presnets each on a newline
        inventory_txt = "\n".join(f"Name: {item.item_name} Damage: {item.item_damage} Rarity {item.item_rarity}" for item in self.inventory) if self.inventory else "Your inventory is empty."
        #popup to display characters inventory
        sg.popup_scrolled("Inventory:", inventory_txt, title="Your Inventory")
        
        
class MonsterTroll(Entity):
    def __init__(self, name="", entity_class="", race="", hit_points=0, damage=0):
        super().__init__(name, entity_class, race)
        self.hit_points = hit_points
        self.damage = damage
        self.attack()
        
        
        
class Dragon(Entity):
    def __init__(self, name="", entity_class="", race="", hit_points=0, damage=0):
        super().__init__(name, entity_class, race)
        self.hit_points = hit_points
        self.damage = damage
        self.attack()
        