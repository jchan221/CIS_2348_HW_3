# Joshua Chan
# 1588459
class Team:
    def __init__(self, name=None, team_wins=0, team_losses=0):
        self.name = name
        self.team_wins = team_wins
        self.team_losses = team_losses
# The arguments are defined in the function above
    def get_win_percentage(self):
        result = self.team_wins / (self.team_wins + self.team_losses)
        return result
# The function above calculates the percentage of wins
if __name__ == '__main__':

    team = Team()
    team.team_name = input()
    team.team_wins = int(input())
    team.team_losses = int(input())
# The class arguments is set to inputs
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team',team.team_name,'has a winning average!')
    else:
        print('Team',team.team_name,'has a losing average.')
# The appropriate response is determined by the if statement above










