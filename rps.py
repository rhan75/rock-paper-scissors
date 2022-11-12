# %%
import random
import re


# %%
def pick_winning_hand(rps_lst: dict) -> str:
    winning_hand = 'draw'
    reduced_lst = set(rps_lst.values())
    if len(reduced_lst) == 2:
        #case 1: rock, paper
        #case 2: rock, scissors
        #case 3: paper, scissors
        if 'rock' in reduced_lst:
            if 'paper' in reduced_lst:
                winning_hand = 'paper'
            else:
                winning_hand = 'rock'
        else:
            winning_hand = 'scissors'
    return winning_hand

# %%
def player_input() -> str:
    rps = {'r': 'rock', 'p': 'paper', 's':'scissors'}
    while True:
        user_input = input('What is your choice? r for rock, p for paper, s for scissors')
        rps_format = re.compile(r'^[r|s|p]$')
        it_is = re.match(rps_format, user_input.lower())
        if it_is:
            break
        else:
            print('Wrong hand selected. Please select a correct hand')
    return str(rps.get(user_input.lower()))

# %%
def determine_num_players() -> int:
    while True:
        how_many = input("How many players are playting this game?")
        #print(type(how_many))
        try:
            return int(how_many)
        except ValueError:
            
            ValueError
            print("Invalid entry. Please try again.")


# %%
def collect_hands(hands: list) -> dict:
    players_hands = {}
    for count, hand in enumerate(hands):
        players_hands[count] = hand
    return players_hands

# %%
def select_winners(winning_hand: str, players_hands: dict) -> list:
    winners = []
    if winning_hand != 'draw':
        for i, (key, value) in enumerate(players_hands.items()):
            if value == winning_hand:
                winners.append(key)
    return winners



# %%
def main():
    #Determine how many players
    num_players = determine_num_players()
    hands_lst = []
    for i in range(num_players):
        hands_lst.append(player_input())
    full_hands = collect_hands(hands_lst)
    winning_hand = pick_winning_hand(full_hands)
    winners = select_winners(winning_hand, full_hands)
    print(winners)

    

# %%
if __name__ == "__main__":
    main()
    



