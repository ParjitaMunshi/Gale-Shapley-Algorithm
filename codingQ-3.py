def stable_matching(teams):
    engaged_teams = {}
    proposers_free = teams.copy()
    
    while proposers_free:
        proposer = proposers_free.pop()
        for responder in teams:
            if responder not in engaged_teams:
                engaged_teams[proposer] = responder
                engaged_teams[responder] = proposer
                break
            else:
                current_partner = engaged_teams[responder]
                if teams.index(responder) > teams.index(current_partner):
                    engaged_teams[proposer] = responder
                    engaged_teams[responder] = proposer
                    proposers_free.append(current_partner)
                    break
    return engaged_teams

# Example usage:
teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H"]
rounds = [16, 8, 4, 2]

for num_teams in rounds:
    engaged_teams = stable_matching(teams[:num_teams])
    for team in engaged_teams:
        if engaged_teams[team] != team:
            teams.remove(team)

print(engaged_teams)
