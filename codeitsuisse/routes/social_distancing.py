import math

def combinations(n, r):
  return math.factorial(n)//math.factorial(r)//math.factorial(n-r)

def helper(seats, people, spaces):

  if ((seats - people)//spaces) <(people -1):
    return 0
  answer = combinations(seats - people + 2 - (people-1)*(spaces-1)-1, people)

  return answer

def socialDistancing():
  # data = request.get_json()

  # inputs = data.get("tests")

  inputs = {
        "0": {
            "seats": 8,
            "people": 3,
            "spaces": 1
        },
        "1": {
            "seats": 7,
            "people": 3,
            "spaces": 1
        },
        "2": {
            "seats": 6,
            "people": 2,
            "spaces": 2
        },
    }

  answers = {}

  for key, value in inputs.items():
    answers[key] = helper(value["seats"], value["people"], value["spaces"])

  # jsonify({"answers": answers})

  return answers
