import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluation():
    data = request.get_json();
    print(data)
    # logging.info("data sent for evaluation {}".format(data))
    # print(result)
    # logging.info("My result :{}".format(result))
    result = []
    for i in range(len(data)):
        dict1 = {}
        dict1['searchItemName'] = data[i].get('searchItemName')
        dict1['searchResult'] = InvtMgmt(data[i].get(
            'searchItemName'), data[i].get('items'))
        result.append(dict1)
    return jsonify(result)

def printPath(dp, word1, word2):
        result = ""
        i = len(word1)
        j = len(word2)

        while(i > 0 or j > 0):
                if word1[i - 1].lower() == word2[j - 1].lower():
                        result = word2[j - 1] + result
                        i -= 1
                        j -= 1

                elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                        result = "+" + word2[j - 1] + result
                        #result = "+" + word2[j - 1] + result
                        j -= 1

                elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                        #result = "-" + word1[i - 1] + result
                        result = "-" + word1[i - 1] + result
                        i -= 1

                elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
                        result = word2[j - 1] + result
                        #result = word2[j - 1] + result
                        i -= 1
                        j -= 1                
        return result

def minDistance(word1, word2):
        dp = [[0 for j in range(len(word2) + 1)]
                                for i in range(len(word1) + 1)]

        for i in range(1,len(word1)+1):
                dp[i][0] = i
        for i in range(1,len(word2)+1):
                dp[0][i] = i

        for i in range(1,len(word1)+1):
                for j in range(1, len(word2) + 1):
                        if word1[i - 1].lower() == word2[j - 1].lower():
                                dp[i][j] = dp[i - 1][j - 1]
                        else:
                                dp[i][j] = min(dp[i - 1][j - 1],
                                       min(dp[i - 1][j], dp[i][j - 1])) + 1

        str1 = printPath(dp, word1, word2)
        lst = str1.split()
        res = ""
        for item in lst:
                if not item[0].isalpha():
                        res += " " + item[0:2] + item[2:].lower()
                else:
                        res += " " + item

        return dp[-1][-1], res.strip()

def InvtMgmt(searchItem, items):
        maximum = len(searchItem)
        dict1 = {}
        for item in items:
                tuple1=minDistance(searchItem, item)
                if len(dict1) >= 10 and tuple1[0] > maximum:
                        continue
                if tuple1[0] not in dict1:
                        dict1[tuple1[0]] = [tuple1[1]]
                        if tuple1[0] < maximum:
                                maximum = tuple1[0]
                else:
                        dict1[tuple1[0]].append(tuple1[1])
        lst = []
        for i in sorted(dict1.keys()):
                if len(lst) >= 10:
                        break
                lst = lst + sorted(dict1[i])
        return lst[0:10]
