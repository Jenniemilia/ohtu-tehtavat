from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from datetime import datetime 


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_sorted()

    print(f"Players from FIN {datetime.now()}")
    print()

    for player in players:
        print(player)    

if __name__ == "__main__":
    main()
