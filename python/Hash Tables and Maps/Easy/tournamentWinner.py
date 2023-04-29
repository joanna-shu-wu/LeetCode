home_team_won=1



# if the team name does not exist in the hash table, add the team as key and assign 3 as value (since it won)
# if the team name exist in the hash table, add 3 to the value
def updateScore(team,point,scoreboard):
	if team not in scoreboard:
		scoreboard[team]=0
	scoreboard[team]=scoreboard[team]+point

def tournamentWinner(competitions, results):
	currentBestTeam=""
    #use a hash table to store the total points collected by each team
	scoreboard={currentBestTeam:0}
    #loop through the competition and update hash table at each iteration.
	for idx,competition in enumerate(competitions):
		result=results[idx]
		homeTeam,awayTeam=competition
		wonTeam=homeTeam if result==home_team_won else awayTeam
		
		updateScore(wonTeam,3,scoreboard)
        # while looping through all the competition, keep track of the team with the highest scores
		if scoreboard[wonTeam]>scoreboard[currentBestTeam]:
			currentBestTeam=wonTeam
    return currentBestTeam

		