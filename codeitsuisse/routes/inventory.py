import Levenshtein

input = [{"searchItemName":"Samsung Aircon","items":["Smsng Auon","Amsungh Aircon","Samsunga Airon"]}]
start = input[0]["searchItemName"].lower()
end = input[0]["items"][2].lower()
s1 = "samsung aircon"
s2 = "amsungh aircon"

Levenshtein.editops(start, end)

# [('insert', 7, 7), ('delete', 11, 12)]
