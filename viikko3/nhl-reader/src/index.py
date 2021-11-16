import requests
from player import Player


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'])

        players.append(player)
        team = Player(
            player_dict['team'])
        players.append(team)

    print(players)

    #print("Oliot:")

    #for player in players:
    #    print(player)    



if __name__ == "__main__":
    main()
