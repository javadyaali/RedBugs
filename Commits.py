
import csv
import time
import traceback
# import os
import requests
import json

pageCount = 652

csv_file = ".csv"
csv_columns = ['sha', 'message', 'author', 'committer', 'tree', 'url', 'comment_count', 'verification']


def writeToFile(result):
    str = ''
    try:
        # if pageCount < 21:
        #     path = 'PR-1.csv'
        # elif pageCount > 20 and pageCount < 41:
        #     path = 'PR-2.csv'
        # elif pageCount > 40 and pageCount < 61:
        #     path = 'PR-3.csv'
        # elif pageCount > 60 and pageCount < 81:
        #     path = 'PR-4.csv'
        # elif pageCount > 80 and pageCount < 101:
        #     path = 'PR-5.csv'
        # elif pageCount > 100 and pageCount < 121:
        #     path = 'PR-6.csv'
        # else:
        path = 'commits.csv'
        with open(path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for dict in result:
                # for data in dict:
                writer.writerow(dict)
    except:
        traceback.print_exc()
        print(str)


url = "https://api.github.com/repos/tensorflow/tensorflow/commits?state=all&per_page=100&page="

try:
    while pageCount < 703:
        response = json.loads(requests.get(url + str(pageCount)).text)

        if len(response) == 2:
            print('limit reached!')
            break

        result = []

        for data in response:
            temp = {'sha' : data['sha'], 'author' : data['commit']['author'], 'committer' : data['commit']['committer']
                , 'message': data['commit']['message'], 'tree' : data['commit']['tree']
                , 'url': data['commit']['url'], 'comment_count' : data['commit']['comment_count']
                , 'verification': data['commit']['verification']}
            result.append(temp)

        print(pageCount)

        writeToFile(result)

        pageCount += 1
        # time.sleep(1)
except Exception:
    # writeToFile()
    traceback.print_exc()

# writeToFile()

