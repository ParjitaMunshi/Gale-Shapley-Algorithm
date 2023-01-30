import time

def stable_matching(super_group1, super_group2):
    engaged_teams = {}
    # Create a list of teams from Super Group 1 who have not yet proposed
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
    return engaged_teams

# Example usage:
super_group1 = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H","Team 1","Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
super_group2 = ["Team I", "Team J", "Team K", "Team L", "Team M", "Team N", "Team O", "Team P","Team 9","Team 10","Team 11","Team 12","Team 13","Team 14","Team 15","Team 16"]

start = time.time()
print(stable_matching(super_group1, super_group2))
end = time.time()
print("Execution time:", end - start)
