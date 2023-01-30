# Gale-Shapley-Algorithm

The World Cup is changing its playoff format using the Gale-Shapley matching algorithm. The eight best teams from groups A,B & C, called Super Group 1, will be matched against the eight best teams from groups D, E & F, called Super Group 2,  using the Gale-Shapley matching algorithm. Further social media will be used to ask fans, media, players and coaches to create a ranking of which teams they would most like to see play their favorite team. 
 
A.	Find a Gale-Shapley implementation in python on Github and modify it so that the eight Super Group 1 teams will be matched against the eight Super Group 2 teams. You can make up the preference lists for each team. Make sure you cite any code you use or state that you wrote it from scratch if you did. 
 
 
 
B.	Use a loop to shuffle the preference lists for each team 1000 times.  Calculate the percentage of stable playoff matches.  See the function random.shuffle(x[, random])   https://docs.python.org/2/library/random.html 
 
 
 
C.	Randomly assume certain teams win and lose each round and eliminate the losers from the preference lists for each team. Can the Gale-Shapley matching algorithm be applied over and over in each round (16 teams, 8 teams, 4 teams, 2 teams) to create stable matches? You can answer this with code or rhetoric. 
 
 
 
D.	Now combine the lists so that any team can be matched against any other irrespective of conference.  Can the Gale-Shapley matching algorithm still create stable matches? (With just one list matching against itself?) You can answer this with code or rhetoric. 
 
 
 
 
E.	Double the size of the lists in problem A several times (you can make up team names like team1, team2, etc.) and measure the amount of time it takes to create stable matches.  How fast does the execution time grow in relation to the size of the lists? 
