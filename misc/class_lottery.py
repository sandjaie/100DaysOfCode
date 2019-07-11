lottery_player_dict = {
    'name': 'Ross', 
    'lottery_numbers': {4, 5, 8}
    }

#Implementing the above in class as blueprint
winning = {1, 4, 2}

class lottery_player:
    def __init__(self, player_name, lottery_numbers):
        self.player_name = player_name
        self.lottery_numbers = lottery_numbers
    
    def find(self):
        inter = self.lottery_numbers.intersection(winning)
        if inter:
            print(f"{self.player_name} has won with winning number: {inter}")
        else:
            print(f"{self.player_name} has no winnings today")

# p1 = lottery_player('Jose', {3,4,5})
# p3 = lottery_player('Ross', {1,3,5})
# p2 = lottery_player('Jack', {0,43,53})

# lottery_player.find(p1)
# lottery_player.find(p2)
# lottery_player.find(p3)

def get_player_info():
    player_name = input("Enter the player name: ")
    lottery_numbers_string = input("Enter the lottery numbers: ").split(',')
    lottery_numbers = [ int(x) for x in lottery_numbers_string]
    return dict(name=player_name, lottery_numbers=set(lottery_numbers))

def get_input():
    player_infos = []
    number_of_players = int(input("Enter the number of players: "))
    for _ in range(number_of_players):
        player_info = get_player_info()
        player_infos.append(player_info)
    return player_infos

def check_winning():
    player_infos = get_input()
    for player in player_infos:
        lottery_player(player['name'], player['lottery_numbers']).find()

if __name__ == "__main__":
    check_winning()
