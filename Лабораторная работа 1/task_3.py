players = ["Harry", "Mike", "Sarah", "Mary", "Jack", "Alex"]

num_players = len(players)

if (num_players % 2 == 0):
    team1 = players[:num_players // 2]
    team2 = players[num_players // 2:]
    print("Команда 1:", team1)
    print("Команда 2:", team2)
else:
    print("It isn't possible to split into equal teams")
