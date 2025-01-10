import re
import sys, os

print("Please provide a path to your cardinals file: ")
path = input()
if path == "":
    print("No path given, please provide a path to your cardinals file.")
namePat = "\w{1,}\s\w{1,}"
batPat = "batted\s(\d+)\stimes"
hitPat = "with\s(\d+)\shits"

# try to open file and catch any errors if it fails
try:
    file = open(path,'r')
except FileNotFoundError:
    print(f"'{str(path)}' does not exist.")
except PermissionError:
    print(f"Permission to access '{str(path)}' denied.")
except Exception as e:
    print(f"Error while opening '{str(path)}':{str(e)}.")

# set up an array for scores
#avgBats = {}
playerScores = {}
playerBats= {}
playerHits = {}
# go through each line in the opened file
for line in file:
    #test beginning of line for the name pattern
    if re.match(namePat, line):
        #assign name pattern match from line to the name variable and wrap as a string
        name = re.match(namePat, line)
        name = str(name.group(0))

        #assign bat pattern match from line to the bats variable and wrap it as an int
        bats = re.search(batPat, line)
        bats = int(bats.group(1))

        #assign hit pattern match from line to the hits variable and wrap it as an int
        hits = re.search(hitPat, line)
        hits = int(hits.group(1))

        if name in playerBats:
            playerBats[name] = playerBats[name] + bats
        else:
            playerBats[name] = int(bats)

        if name in playerHits:
            playerHits[name] = playerHits[name] + hits
        else:
            playerHits[name] = int(hits)
        batting_average = float(playerHits[name]/playerBats[name])
        playerScores[name] = (batting_average)

sortedScores = sorted(playerScores.items(), key = lambda item: item[1], reverse=True)
for key, val in sortedScores:
    print(f'%s : %.3f' %(key, val))