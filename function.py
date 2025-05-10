import random
import player_monster
import question


class function:
    def __init__(self, player_name: str, monster_attack: int, difficulty: str, game_status):
        self.player_status = player_monster.Player(player_name)
        self.monster_status = player_monster.Monster(monster_attack)
        self.difficulty = difficulty.upper()
        self.game_status = game_status

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

    # decreases the monster's health by player attacked, where it can't fall below 0.
    def damage_monster(self):
        if self.monster_status.hp > 0:
            # If there is blood, damage reduction (monster attack power)
            self.monster_status.hp -= self.player_status.attack

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
        if symbols == '0':
            self.player_status.x = coordinate_x  # update player location
            self.player_status.y = coordinate_y
            return True

        # player meet door
        # if difficulty is normal level or hell level, then judge if player x,y is maze size, update (0,0)
        elif symbols == 'D':
            self.player_status.x = coordinate_x
            self.player_status.y = coordinate_y
            print(f"{self.player_status.name} have escaped from the maze")
            return True

        # meet wall, cant pass
        elif symbols == '1':
            print("It's wall, Cannot move!")
            return False

        # met monster part
        elif symbols == 'M':
            print("You encountered a monster!")

            # ask question
            if question.ask_question():
                self.player_status.attack = random.randint(5, 10)
                print(f"Correct! Your attack power is now {self.player_status.attack}")
            else:
                print("Wrong answer! You have no attack power and will take damage.")
                self.player_status.attack = 0

            # Generate a new monster for each battle (to avoid health duplication)
            monster = player_monster.Monster(self.monster_status.attack)
            print(f"Monster HP: {monster.hp}, Attack: {monster.attack}")

            round_count = 1
            # Combat cycle: until one side dies
            while self.player_status.hp > 0 and monster.hp > 0:
                print(f"-- Round {round_count} --")

                # player attack player
                monster.hp -= self.player_status.attack
                monster.hp = max(monster.hp, 0)
                print(f"Player dealt {self.player_status.attack} damage. Monster HP: {monster.hp}")

                # if monster die, break out
                if monster.hp <= 0:
                    if self.difficulty == 'SIMPLE':
                        self.has_key()
                    elif self.difficulty == 'NORMAL' and self.game_status.current_level == 3:
                        self.has_key()
                    elif self.difficulty == 'HELL' and self.game_status.current_level == 5:
                        self.has_key()
                        print("You obtained the key!")

                    self.player_status.x = coordinate_x
                    self.player_status.y = coordinate_y
                    break

                # monster attack player
                self.player_status.hp -= monster.attack
                self.player_status.hp = max(self.player_status.hp, 0)
                print(f"Monster dealt {monster.attack} damage. Your HP: {self.player_status.hp}")
                round_count += 1

            if self.player_status.hp <= 0:
                print(f"{self.player_status.name} has fallen.")
                return False

            else:
                print(f"{self.player_status.name} successfully killed the monster. Your HP: {self.player_status.hp}/10")
                self.player_status.x = coordinate_x
                self.player_status.y = coordinate_y
                return True

        else:
            return False



