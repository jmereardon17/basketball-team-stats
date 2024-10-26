def balance(players, teams):
  experienced_players = list(filter(lambda player: player["experience"], players))
  inexperienced_players = list(filter(lambda player: not player["experience"], players))
  players_per_team = len(players) // len(teams)
  balanced_teams = []

  for team_name in teams:
    team = { 'name': team_name, 'players': [] }
  
    for _ in range(players_per_team // 2):
      if experienced_players:
        team['players'].append(experienced_players.pop())
      if inexperienced_players:
        team['players'].append(inexperienced_players.pop())

    balanced_teams.append(team)

  return balanced_teams

def show_stats(team):
  players = ", ".join([player['name'] for player in team['players']])
  experienced_players = [player for player in team['players'] if player['experience']]
  inexperienced_players = [player for player in team['players'] if not player['experience']]
  player_heights = [player['height'] for player in team['players']]
  average_player_height = sum(player_heights) / len(player_heights)
  guardians = ", ".join(guardian for player in team['players'] for guardian in player['guardians'])

  print(f"\nTeam: {team['name']}")
  print("--------------------")
  print(f"Total players: {len(team['players'])}")
  print(f"Inexperienced players: {len(inexperienced_players)}")
  print(f"Experienced players: {len(experienced_players)}")
  print(f"Average player height: {average_player_height:.2f}\n")
  print("Players:")
  print(f"{players}\n")
  print("Guardians:")
  print(f"{guardians}\n")