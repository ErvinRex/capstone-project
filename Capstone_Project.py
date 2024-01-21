"""                                   /@
                     __        __   /\/
                    /==\      /  \_/\/   
                  /======\    \/\__ \__
                /==/\  /\==\    /\_|__ \
             /==/    ||    \=\ / / / /_/
           /=/    /\ || /\   \=\/ /     
        /===/   /   \||/   \   \===\
      /===/   /_________________ \===\
   /====/   / |                /  \====\
 /====/   /   |  _________    /  \   \===\    THE LEGEND OF 
 /==/   /     | /   /  \ / / /  __________\_____      ______       ___
|===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \
 \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \
 \===\__    \    /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \
   \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \
   \===\ \   \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
     \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ |
     \==\     _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | |
       \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | |
       \==\ /   / / /________/ |/_________|/_________|/_____/   /___\ /___\
         \==\  /               | /==/
         \=\  /________________|/=/    
           \==\     _____     /==/ 
          / \===\   \   /   /===/
         / / /\===\  \_/  /===/
        / / /   \====\ /====/
       / / /      \===|===/
       |/_/         \===/
                      ="""


import random


class ganon:
    def __init__(self, attack=0, speed=0, defence=0, health=0):
        # Initialise Ganon's attributes with default values or values provided during instantiation
        self.attack = 5
        self.speed = 2
        self.defence = 10
        self.health = 80

    def ganon_attack(self):
        # Calculate Ganon's attack based on his base attack, speed, and a multiplier
        attack = self.attack
        return attack * (self.speed * 1.25)

    def ganon_defend(self):
        # Calculate Ganon's defense based on his base defense, speed, and a multiplier
        defence = self.defence
        return defence * (self.speed * 1.25)

    def ganon_action(self):
        # Randomly choose an action for Ganon from a list of options
        return random.choice(['strike', 'protect'])


class link:
    def __init__(self, attack=0, speed=0, defence=0, health=0):
        # Initialise Link's attributes with default values or values provided during instantiation
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.health = 60

    def build_selection(self):
        # Allow the player to choose a character build (attack or defense) and return corresponding values
        builds = {'attack': [6, 3, 1], 'defence': [3, 1, 7]}
        build = builds.get(
            input("Pick a character build: 'Attack' or 'Defence'").lower())
        if build:
            attack, speed, defence = build
            return attack, speed, defence
        else:
            raise ValueError  # Raise a value error if the build type is invalid

    def link_build(self):
        # Set Link's attributes based on the chosen character build
        build = self.build_selection()
        self.attack, self.speed, self.defence = build
        return build

    def link_action(self):
        # Allow the player to choose an action for Link (strike or protect) and return the chosen action
        action = input("'Strike' Ganon or 'Protect' against his strikes?:")
        return action.lower()

    def critical(self):
        # Determine whether Link's attack is a critical hit (1 in 3 chance of doubling the damage)
        chance = random.randrange(1, 4)
        if chance == 3:
            return 2  # Return 2 for critical hit, doubling the damage
        else:
            return 1  # Return 1 for normal damage

    def link_attack(self):
        # Calculate Link's attack based on critical hit chance, attack, speed, and a multiplier
        return (self.attack * self.critical()) * (self.speed * 1.25)

    def link_defend(self):
        # Calculate Link's defense based on critical hit chance, defense, speed, and a multiplier
        defence = self.defence
        return defence * self.critical() * (self.speed * 1.25)


# Variables for Link and Ganon
hero = link()
enemy = ganon()


# Battle script
def battle_script():
    # Display introductory messages for the battle
    print('Calamity Ganon has become enraged, muster up any strength you have and defeat him before he destroys Hyrule Kingdom!')
    print('Before the battle begins, decide which character build you would like to use...')
    print("The 'Attack' build (+6 attack, +3 speed, +1 defence) or the 'Defence' build (+3 attack, +1 speed, +7 defence)")

    # Get the attack, speed, and defence from the chosen build to use in the battle
    attack, speed, defence = hero.link_build()

    # Main battle loop, continues until either hero or enemy's health drops to zero
    while hero.health > 0 and enemy.health > 0:
        # Player and enemy actions during the battle
        hero_action = hero.link_action()
        enemy_action = enemy.ganon_action()

        # Calculate and apply damage based on enemy's action
        if enemy_action == 'strike':
            enemy_damage = enemy.ganon_attack()
            hero.health -= enemy_damage
        elif enemy_action == 'protect':
            enemy_damage = enemy.ganon_defend()
            enemy.health += enemy_damage

        # Calculate and apply damage based on player's action
        if hero_action == 'strike':
            link_damage = hero.link_attack()
            enemy.health -= link_damage
            # Display the outcome of the round
            print(
                f"You decided to {hero_action} for {link_damage} damage, whilst Calamity Ganon has decided to {enemy_action} for {enemy_damage}!")
        elif hero_action == 'protect':
            link_protect = hero.link_defend()
            hero.health += link_protect
            # Display the outcome of the round
            print(
                f"You decided to {hero_action} for {link_protect} damage, whilst Calamity Ganon has decided to {enemy_action} for {enemy_damage}!")

        # Display current health of both hero and Calamity Ganon
        print(
            f"Your health is {hero.health}, Calamity Ganon's health is {enemy.health}")

    # Determine the outcome of the battle
    if hero.health <= 0:
        print("Calamity Ganon has defeated yet another hero!\nHyrule Kingdom is doomed!")
    else:
        print("Calamity Ganon has finally been defeated!\nHyrule Kingdom is saved!")


# Start the battle script
battle_script()
