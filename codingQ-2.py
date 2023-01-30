import random

def stable_matching(super_group1, super_group2):
    # Create a dictionary to store the current engagement of each team
    engaged_teams = {}
    # Create a list of teams from Super Group 1 who have not yet proposed
    proposers_free = super_group1.copy()
    # Create a variable to store the number of stable matches
    stable_matches = 0
    
    for i in range(100000):
        # Shuffle the teams in both Super Group 1 and Super Group 2
        random.shuffle(super_group1)
        random.shuffle(super_group2)
        
        # Reset the engaged teams and proposers_free for each iteration
        engaged_teams = {}
        proposers_free = super_group1.copy()
        
        # While there are still teams from Super Group 1 who have not proposed
        while proposers_free:
            # Pop a team from the list of teams from Super Group 1 who have not proposed
            proposer = proposers_free.pop()
            
            # Iterate through the teams from Super Group 2
            for responder in super_group2:
                # If the team from Super Group 2 is not engaged
                if responder not in engaged_teams:
                    # Engage the teams
                    engaged_teams[proposer] = responder
                    engaged_teams[responder] = proposer
                    break
                else:
                    # If the team from Super Group 2 is already engaged
                    current_partner = engaged_teams[responder]
                    # Check if the team from Super Group 1 is a better match for the team from Super Group 2
                    if current_partner in super_group2 and super_group2.index(responder) > super_group2.index(current_partner):
                        # Engage the teams
                        engaged_teams[proposer] = responder
                        engaged_teams[responder] = proposer
                        # Add the current partner to the list of teams from Super Group 1 who have not yet proposed
                        proposers_free.append(current_partner)
                        break
        # check if the match is stable or not
        if set(engaged_teams.keys()) == set(super_group1):
            stable_matches += 1
    # return percentage of stable match
    return stable_matches/1000

# Example usage:
super_group1 = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H"]
super_group2 = ["Team I", "Team J", "Team K", "Team L", "Team M", "Team N", "Team O", "Team P"]

# Run the function multiple times to get a better understanding of the probability of a stable match
results = []
for i in range(100):
    results.append(stable_matching(super_group1, super_group2))

# Calculate the average of the returned values
average = sum(results) / len(results)

print(average)
