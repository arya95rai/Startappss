# # 3. Create a Team class and a Player class. 
# # Add multiple players to a team and display all player names.
# class Team:
#     def __init__(self,team_name,player_name):
#         self.team_name=team_name
#         self.player_name=self.player_name
#     def add_player(self,new_player):
#         self.player_name.append(new_player)
#     def display(self):
#         print(f"Team: {self.team_name}")
#         print(f"Players: {self.player_name}")
    
# class Player(self,name):
#     def __init__(self,name):
#         self.player_name=name

    

import logging

# Configure logging
logging.basicConfig(
    filename="file.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Parameters:
# filename : Name of the log file
# level    : DEBUG, INFO, WARNING, ERROR, CRITICAL
# format   : Log message format
# filemode : "a" (append, default), "w" (overwrite)

# DEBUG    : Detailed debugging information
# INFO     : General application events
# WARNING  : Something unexpected happened, but the program continues
# ERROR    : An error occurred
# CRITICAL : Very serious error; application may stop

try:
    result = 100 / 0

except ZeroDivisionError:
    logging.exception("Division by Zero occurred")