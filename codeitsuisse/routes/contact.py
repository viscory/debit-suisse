# input = {
#     "infected": {
#         "name":"orange",
#         "genome":"acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
#     },
#     "origin": {
#         "name":"turquoise",
#         "genome":"acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
#     },
#     "cluster":[
#         {
#             "name":"magenta",
#             "genome":"acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
#         }
#     ]
# }

input = {
    "infected": {
        "name":"plastic",
        "genome":"acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
    },
    "origin": {
        "name":"metal",
        "genome":"acg-acu-uca-gca-acu-ccc-gua-acg-ccu-uca-gca-acu-cac-gac"
    },
    "cluster":[
        {
            "name":"thread",
            "genome":"acg-acu-uca-gca-acu-ccc-gua-acg-ccu-uca-gca-acu-cac-gaa"
        }
    ]
}


import math

def difference(a, b):

  startDiff = 0
  middleDiff = 0

  splitA = a.split("-")
  splitB = b.split("-")

  for i in range(len(splitA)):
    smallA = splitA[i]
    smallB = splitB[i]

    if smallA[0] != smallB[0]:
      startDiff += 1
    
    if smallA[1] != smallB[1]:
      middleDiff += 1

    if smallA[2] != smallB[2]:
      middleDiff += 1

  totalDiff = startDiff + middleDiff

  return (totalDiff, startDiff)

def recursor(infected, genes, answer, path, visited):
  minimumDiff = math.inf
  possibilities = []
  finalChecker = []

  if(len(visited) == len(genes)):
    path = path+infected["name"]
    answer.append(path)
    # print(visited)
    return

  if(infected["name"] == "metal"):
    path = path+infected["name"]
    answer.append(path)
    return

  for i in genes:

    if(i["name"] not in visited):
      # print("finding difference for ", i["name"])
      currentDiff = difference(infected["genome"], i["genome"])

      finalChecker.append((i, currentDiff))

      if currentDiff[0] < minimumDiff:
        minimumDiff = currentDiff[0]
  
  for i in finalChecker:
    if i[1][0] == minimumDiff:
      possibilities.append(i)
    
  for point in possibilities:
    # ["plastic* -> thread -> metal"]

    if (point[1][0] == 0):
      answer.append(path + infected["name"] + " -> " + point[0]["name"])
      continue

    if (point[1][1]> 0):
      recursor(point[0], genes, answer, path+infected["name"] + "* -> ", visited + [point[0]["name"]])
    else:
      recursor(point[0], genes, answer, path+infected["name"] + " -> ", visited + [point[0]["name"]])
    
    

def contact(input):

  infected = input["infected"]

  origin = input["origin"]

  cluster = input["cluster"]

  genes = [origin] + [c for c in cluster] 

  # gene, non-Silent
  answer = []

  path = ""

  visited = []

  recursor(infected, genes, answer, path, visited)

  print(answer)

  
contact(input)




