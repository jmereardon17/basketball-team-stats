import copy

def clean(players):
  players_copy = copy.deepcopy(players)

  for player in players_copy:
    player["guardians"] = get_arr_from_string(player["guardians"], " and ")
    player["experience"] = player["experience"].upper() == "YES"
    player["height"] = get_int_from_string(player["height"])
    
  return players_copy

def get_int_from_string(string):
  return int(''.join(filter(str.isdigit, string)))

def get_arr_from_string(string, pattern = " "):
  return string.split(pattern)
