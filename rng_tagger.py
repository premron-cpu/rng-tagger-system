import random

# List of players
players = []

# Add players
def add_player(name):
    players.append(name)

# Choose tagger
def choose_tagger():
    if len(players) == 0:
        print("No players added!")
        return
    
    tagger = random.choice(players)
    print("Tagger is:", tagger)

# Example usage
add_player("Prem")
add_player("Alex")
add_player("John")
add_player("Sam")

choose_tagger()
