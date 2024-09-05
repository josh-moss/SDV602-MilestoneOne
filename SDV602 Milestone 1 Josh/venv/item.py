#this entire class is probably extremely unnecessary i like it so it stays
#super class item holds all the common attributes and methods for each item
class Item:
    def __init__(self, item_name="", item_rarity="", item_damage=0, item_value=0):
        self.item_name = item_name
        self.item_rarity = item_rarity
        self.item_damage = item_damage
        self.item_value = item_value
    
    #this tuple could be used to print all levels of rare items in game 
    available_rarities = ("Common", "Rare", "Legendary")

#subclass of item, provides defaults for any sword instance to inherit from 
class Sword(Item):
    def __init__(self, item_name="", item_rarity="", item_damage=0, item_value=0, blade_type=""):
        super().__init__(item_name, item_rarity, item_damage, item_value)
        self.blade_type = blade_type
    
    
class Shield(Item):
    def __init__(self, item_name="", item_rarity="", item_damage=0, item_value=0, shield_type=""):
        super().__init__(item_name, item_rarity, item_damage, item_value)
        self.shield_type = shield_type
    
    
class Bow(Item):
    def __init__(self, item_name="", item_rarity="", item_damage=0, item_value=0, bow_type=""):
        super().__init__(item_name, item_rarity, item_damage, item_value)
        self.bow_type = bow_type
    
class Artifact(Item):
    def __init__(self, item_name="", item_rarity="", item_damage=0, item_value=0, artifact_type=""):
        super().__init__(item_name, item_rarity, item_damage, item_value)  
        self.artifact_type = artifact_type
    
    
class WeaponInstance:
    def __init__(self):
        self.game_items()
        
    def game_items(self):
        # Weapon instances for the gameworld
        self.swords = [
            Sword(item_name="Great Sword", item_rarity="Lengendary", item_damage=20, item_value=500, blade_type="Colossal Blade"),
            Sword(item_name="Long Sword", item_rarity="Rare", item_damage=10, item_value=250, blade_type="Long Blade")
        ]
        
        self.shields = [
            Shield(item_name="Great Shield", item_rarity="Rare", item_damage=0, item_value=100, shield_type="Colossal Shield"),
            Shield(item_name="Wood Shield", item_rarity="Common", item_damage=0, item_value=20, shield_type="Small Shield")
        ]
        
        self.bows = [
            Bow(item_name="Long Bow", item_rarity="Common", item_damage=5, item_value=50, bow_type="Large Bow"),
            Bow(item_name="Short Bow", item_rarity="Common", item_damage=3, item_value=25, bow_type="Small Bow")
        ]
        
        self.keys = [
            Artifact(item_name="Rusty Key", item_rarity="Common", item_damage=0, item_value=10, artifact_type="Key"),
            Artifact(item_name="Diamond Key", item_rarity="Rare", item_damage=0, item_value=150, artifact_type="Key")
        ]