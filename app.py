import sys
import string
from constants import TEAMS, PLAYERS
from utils.data import clean
from utils.teams import balance, show_stats

def get_choice(choices):
  choice = input("\nEnter an option:  ").upper()

  while choice not in choices:
    choice = input("Please choose a valid option:  ").upper()

  return choice

def main():
  players = clean(PLAYERS)
  balanced_teams = balance(players, TEAMS)
  print("BASKETBALL TEAM STATS TOOL\n")

  while True:
    print("\n----MENU----\n")
    print("""Choose an option:
  A) Display Team Stats
  B) Quit
    """)
      
    choice = get_choice({"A", "B"})
    if choice == "A":
      team_choices = {index: team for index, team in zip(string.ascii_uppercase, balanced_teams)}

      print("\n---TEAMS---\n")
      for index, team in team_choices.items():
        print(f"{index}) {team['name']}")

      choice = get_choice(team_choices.keys())
      team_index = ord(choice) - ord("A")
      team = balanced_teams[team_index]
      show_stats(team)

      choice = input("Press ENTER to continue...")

      while choice != "":
        choice = input("Press ENTER to continue...")
      continue
    else: sys.exit(0)

if __name__ == '__main__':
  main()