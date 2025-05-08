import player_monster


class function:
    def __init__(self, player_name: str, monster_attack: int):
        self.player_status = player_monster.Player(player_name)
        self.monster_status = player_monster.Monster(monster_attack)

    # Returns True if the player has no hp (reaches 0), otherwise False
    def player_is_out_of_hp(self) -> bool:
        if self.player_status.hp <= 0:
            return True
        else:
            return False

    # Returns True if the monster has no hp (reaches 0), otherwise False
    def monster_is_out_of_hp(self) -> bool:
        if self.monster_status.hp <= 0:
            return True
        else:
            return False

    # decreases the player's health by monster attacked, where it can't fall below 0.
    def damage_player(self):
        if self.player_status.hp > 0:
            # If there is blood, damage reduction (monster attack power)
            self.player_status.hp -= self.monster_status.attack

    # marks that player has got key
    def has_key(self):
        self.player_status.has_key = True

    # player interaction based on symbols and coordinate.
    # Each interaction change player's state (coordinate, hp, attack, has_key).
    def interact(self, symbols: str, coordinate_x: int, coordinate_y: int) -> bool:
        # Parameters:
        #     symbol (str): The symbol representing the entity ('0', '1', 'M', 'D')
        #     symbol_x (int): The x-coordinate of the entity
        #     symbol_y (int): The y-coordinate of the entity

        # Return:
        #     bool: True if the player moves to the coordinate, otherwise False
        if symbols == 'o':
            self.x = coordinate_x  # update player location
            self.y = coordinate_y
            return True

        elif symbols == 'D':
            self.land_at_destination()
            self.x = coordinate_x
            self.y = coordinate_y
            print(f"{self.name} has reached: Sector 9-Delta")
            return True

        elif symbols == '.':
            print("Cannot move past an asteroid!")
            return False

        elif symbols == 'E':
            self.consume_fuel()  # fuel -1
            self.damage_ship()  # health -1
            self.x = coordinate_x
            self.y = coordinate_y
            if self.is_out_of_health():  # health == 0
                print(f"{self.name} has fallen.")
            else:
                print(f"We won the fight! Health: {self.health}/3")  # health > 0
            return True

        elif symbols == 'M':
            self.consume_fuel()  # fuel -1
            self.add_mineral()  # mineral +1
            self.x = coordinate_x
            self.y = coordinate_y
            print(f'+1 mineral! Minerals: {self.minerals}')
            return True

        elif symbols == 'R':
            if self.health == 3:
                print("Ship is already at full health!")
                return False
            elif self.health != 3 and self.minerals == 0:
                print("You need a mineral to activate this repair station.")
                return False
            elif self.health != 3 and self.minerals > 0:
                self.consume_fuel()  # fuel -1
                self.use_mineral()  # mineral -1
                self.x = coordinate_x  # update ship location
                self.y = coordinate_y
                self.repair_ship()  # health +1
                print(f'Ship repaired! Health: {self.health}/3')
                return True
        else:
            return False



