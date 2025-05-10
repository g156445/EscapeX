'''
Track the current level and determine if there is a next level:
    If there is a next level, current_level + 1, and return True.
    If it is the last level, issue the key (has_key=True), output the prompt, and return False.
'''

class game_continue:
    def __init__(self):
        self.current_level = 1      # set starting from 1
        self.total_levels = {
            'SIMPLE': 1,
            'NORMAL': 3,
            'HELL': 5
        }
        self.has_key = False

    def continue_maze(self, difficulty: str) -> bool:
        if self.current_level < self.total_levels[difficulty.upper()]:
            self.current_level += 1
            # If there is a next level, continue into the maze.
            return True
        else:
            self.has_key = True
            print("Player Obtained the key")
            # If there is no next level, clear the level
            return False
