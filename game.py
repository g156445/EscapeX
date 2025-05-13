import random
import maze
import game_continue
import function


# show map; 'P' is player; '.' is path; '#' is walls
def print_map(current_maze, player_x, player_y):
    for y, row in enumerate(current_maze):
        line = ''
        for x, val in enumerate(row):
            if x == player_x and y == player_y:
                line += 'P '  # player location
            elif val == 0:
                line += '. '  # convert path
            elif val == 1:
                line += '# '  # convert wall
            elif val == 'M':
                line += 'M '
            elif val == 'D':
                line += 'D '
        print(line)
    print()

def main():
    game_status = game_continue.game_continue()
    difficulty = input("Please select difficulty (SIMPLE / NORMAL / HELL): ").upper()

    # select maze difficulty
    if difficulty == "SIMPLE":
        mazes = [maze.maze1]
    elif difficulty == "NORMAL":
        mazes = [maze.maze1, maze.maze2, maze.maze3]
    elif difficulty == "HELL":
        mazes = [maze.maze1, maze.maze2, maze.maze3, maze.maze4, maze.maze5]
    else:
        print("Invalid difficulty selected.")
        return

    # Initialize player and monster according difficulty
    player_name = input("Enter your player name: ")
    if difficulty == "SIMPLE":
        monster_attack = 2
    elif difficulty == "NORMAL":
        monster_attack = 4
    else:
        monster_attack = 6
    logic = function.function(player_name, monster_attack, difficulty, game_status)
    logic.player_status.attack = random.randint(5, 10)
    print(f"At the beginning game, initial attack power is:{logic.player_status.attack}")

    x = 0
    y = 0
    # enter maze list
    for level_maze in mazes:
        print(f"=== Level {game_status.current_level} Start ===")

        while True:
            # show map and show command
            print_map(level_maze, x, y)
            print("Command: (w/s/a/d to move, 'status' to show player info)")
            command = input("Your move: ").lower()
            new_x = x
            new_y = y
            if command == "status":
                # show player_monster status
                print(logic.player_status)
                continue

            elif command == "w":
                new_y -= 1
            elif command == "s":
                new_y += 1
            elif command == "d":
                new_x += 1
            elif command == "a":
                new_x -= 1
            else:
                print("Invalid command.")
                continue

            # Boundary Detection
            if not (0 <= new_x < 8 and 0 <= new_y < 8):
                print("It's wall, Cannot move!")
                continue

            symbol = str(level_maze[new_y][new_x])
            moved = logic.interact(symbol, new_x, new_y, level_maze)
            if moved == "NEXT":
                x = 0
                y = 0
                break  # kill current while loop, into next map

            elif moved:
                x = new_x
                y = new_y

            # when player's hp <= 0, game over
            if logic.player_is_out_of_hp():
                print("Game Over! You died.")
                return

            # fix bug: player arrived door but no key -> can't escape maze
            if not logic.player_status.has_key and logic.player_status.x == len(maze.maze1) - 1 and logic.player_status.y == len(maze.maze1) - 1:
                print("Need Key to Open door!")

            # Check if the player has the key and escapes from this level
            if logic.player_status.has_key and logic.player_status.x == len(maze.maze1) - 1 and logic.player_status.y == len(maze.maze1) - 1:
                if game_status.continue_maze(difficulty):
                    x = 0
                    y = 0
                    break
                else:
                    print("Congratulations! You escape the maze.")
                    return

if __name__ == "__main__":
    main()
