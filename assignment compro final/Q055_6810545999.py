# Name: Inthat # Student ID: 68010545999

class Player:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        
class Team:
    def __init__(self, team_name):
        self.__team_name = team_name
        self.__player = []
    def add_player(self, player_name, skill):
        Added = None
        for p in self.__player:
            if p.name == player_name:
                Added = False
                break
        if Added == None:
            Added = True
            player = Player(player_name, skill)
            self.__player.append(player)
        return Added
    def remove_player(self, player_name):
        removed = None
        for s in self.__player:
            if s.name == player_name:
                self.__player.remove(s)
                removed = True
            else:
                removed = False
        return removed
    
    def get_report(self):
        print('--- Team Report ---')
        print(f"Team {self.__team_name}")
        print(f'Players: {len(self.__player)}')
        total = 0
        for p in self.__player:
            total += p.skill
        average = total/len(self.__player)
        if average == 0 or average < 0:
            print('Average Skill: 0.0')
        else:
            print(f'Average Skill: {(total/len(self.__player)):.1f}')
league = {}

while True:
    parts = input("Enter command: ").split()
    if not parts:
        print('Error: Invalid command.')
        continue
    command = parts[0]
    
    if command.lower() == 'exit':
        print("Goodbye.")
        break
    elif command.lower() == 'addteam':
        team_n = parts[1]
        if team_n in league:
            print(f"Error: Team {team_n} already exists.")
        else:
            league[team_n] = Team(team_n)
            print(f"Team {team_n} created.")
            

    elif command.lower() == 'addplayer':
        team_n = parts[1]
        p_name = parts[2]
        value = int(parts[3])
        try:
            added = league[team_n].add_player(p_name, value)
            if added is True:
                print(f"Player {p_name} added to {team_n}.")
        except:
            print('Error: Team not found.')

    elif command.lower() == 'removeplayer':
        team_n = parts[1]
        p_name = parts[2]
        try:
            removed = league[team_n].remove_player(p_name)
            if removed is True:
                print(f'Player {p_name} removed from {team_n}.')
        except:
            print(f'Error: Player {p_name} not found on team.')
    
            
    elif command.lower() == 'report':
        team_n = parts[1]
        try:
            league[team_n].get_report()
        except:
            print('Error: Team not found.')

    else:
        print('Error: Invalid command.')