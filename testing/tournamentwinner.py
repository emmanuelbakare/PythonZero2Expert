import collections
def tournamentwinner(matches, results):
    winner=collections.defaultdict(int)
    # winner={}
    for k in range(len(matches)):
        if results[k]==0:
            currWin=winner[matches[k][1]]
            # winner[matches[k][1]]+=3 if winner[matches[k][1]] in winners else winner[matches[k][1]]=3
            winner[matches[k][1]]+=3
            # currWin+=3
        else:
            # winner[matches[k][0]]+=3 if result[k] in winners else winner[matches[k][0]]=3
            currWin=winner[matches[k][0]]
            # currWin+=3 
            winner[matches[k][0]]+=3 
    return max(winner, key=winner.get)


#Another Solution
HOME_TEAM_WON=1
def tournamentwinner_two(competitions, results):   
    currentBestTeam=""
    scores={currentBestTeam:0}
    
    for idx,competition in enumerate(competitions):
        result=results[idx]
        hometeam, awayteam=competition
        
        winingTeam=hometeam if result==HOME_TEAM_WON else awayteam
        
        updatescores(winingTeam,3,scores)
        if scores[winingTeam] > scores[currentBestTeam]:
            currentBestTeam= winingTeam
    return currentBestTeam
    # return scores

def updatescores(team, point, scores):
    if team not in scores:
        scores[team]=point
    else:
        scores[team] +=point
            
        # print(winingTeam,awayteam,homeTeam)
         
        
matches1=[["HTML","C#"], ["C#", "Python"],["Python","HTML"]]
result1=[0,0,1]

matches2=[["HTML", "Java"],["Java", "Python"],["Python", "HTML"]]
result2=[0, 1, 1]

matches3=[
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"],
  ["C#", "Python"],
  ["Java", "C#"],
  ["C#", "HTML"]
]
result3=[0, 1, 1, 1, 0, 1]

matches4=[
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"],
  ["C#", "Python"],
  ["Java", "C#"],
  ["C#", "HTML"],
  ["SQL", "C#"],
  ["HTML", "SQL"],
  ["SQL", "Python"],
  ["SQL", "Java"]
]
result4=[0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

matches5=[
  ["Bulls", "Eagles"]
]
result5=[1]


matches6=[
  ["Bulls", "Eagles"],
  ["Bulls", "Bears"],
  ["Bears", "Eagles"]
]
result6=[0, 0, 0]

matches7=[
  ["Bulls", "Eagles"],
  ["Bulls", "Bears"],
  ["Bulls", "Monkeys"],
  ["Eagles", "Bears"],
  ["Eagles", "Monkeys"],
  ["Bears", "Monkeys"]
]
result7=[1, 1, 1, 1, 1, 1]

matches8=[
  ["AlgoMasters", "FrontPage Freebirds"],
  ["Runtime Terror", "Static Startup"],
  ["WeC#", "Hypertext Assassins"],
  ["AlgoMasters", "WeC#"],
  ["Static Startup", "Hypertext Assassins"],
  ["Runtime Terror", "FrontPage Freebirds"],
  ["AlgoMasters", "Runtime Terror"],
  ["Hypertext Assassins", "FrontPage Freebirds"],
  ["Static Startup", "WeC#"],
  ["AlgoMasters", "Static Startup"],
  ["FrontPage Freebirds", "WeC#"],
  ["Hypertext Assassins", "Runtime Terror"],
  ["AlgoMasters", "Hypertext Assassins"],
  ["WeC#", "Runtime Terror"],
  ["FrontPage Freebirds", "Static Startup"]
]
result8=[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

matches9=[
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"],
  ["C#", "Python"],
  ["Java", "C#"],
  ["C#", "HTML"],
  ["SQL", "C#"],
  ["HTML", "SQL"],
  ["SQL", "Python"],
  ["SQL", "Java"]
]
result9=[0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

matches10=[
  ["A", "B"]
]
result10=[0]

# print(tournamentwinner(matches1,result1))
# print(tournamentwinner_two(matches1,result1)) 

# print(timeit.timeit())
k=[1/2,1/3]

# print(sum(k)/len(k))

# tup=(1,2,3)
# tup+=(4,5,6)
# print(tup)

def multipliers(): 
    return [lambda x : i * x for i in range(4)] 

print([m(2) for m in multipliers()])