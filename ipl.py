import pandas as pd
import numpy as np
import json
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)
# print(matches)


def teamsAPI():
    teams= list(set(list(matches["Team1"]) + list(matches["Team2"])))
    team_dict = {
        "teams":teams
    }
    return team_dict


def team_vs_team(team1,team2):
    valid_team= list(set(list(matches["Team1"]) + list(matches["Team2"])))

    if ((team1 in valid_team )and (team2 in valid_team)) :
    
        temp_df=matches[(matches["Team1"]==team1) & (matches["Team2"]==team2) | (matches["Team1"]==team2) & (matches["Team2"]==team1)]
        
        total_matches=temp_df.shape[0]
        team1_won=temp_df["WinningTeam"].value_counts()[team1]
        team2_won=temp_df["WinningTeam"].value_counts()[team2]
        draws= total_matches - (team1_won+team2_won)
        print(11)
        response ={
            "total_matches" : str(total_matches),
            team1 : str(team1_won),
            team2 : str(team2_won),
            "draws" : str(draws)
        }


        return response
    else:
        return   {"measage" : "invalid team"}

# team_vs_team("Chennai Super Kings","Mumbai Indians")