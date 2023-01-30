import numpy as np

# Assume we have a list of 16 teams
teams = ["team1", "team2", "team3", "team4", "team5", "team6", "team7", "team8", "team9", "team10", "team11", "team12", "team13", "team14", "team15", "team16"]

# Create a dictionary to store the preference list of each team
pref_lists = {}
for team in teams:
    np.random.shuffle(teams)
    pref_lists[team] = teams.copy()

# Implement the Gale-Shapley algorithm
def stable_matching(pref_lists):
    n = len(pref_lists)
    free_teams = list(pref_lists.keys())
    matches = {}
    while free_teams:
        team = free_teams.pop(0)
        for candidate in pref_lists[team]:
            if candidate not in matches:
                matches[candidate] = team
                break
            else:
                current_partner = matches[candidate]
                if pref_lists[candidate].index(team) < pref_lists[candidate].index(current_partner):
                    matches[candidate] = team
                    free_teams.append(current_partner)
                    break
    return matches

# Call the function and print the matches
print(stable_matching(pref_lists))
