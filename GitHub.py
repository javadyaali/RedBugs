#
# from github import Github
#
# # using username and password
# # g = Github("", "")
#
# # or using an access token
# # g = Github("access_token")
#
# # Github Enterprise with custom hostname
# # g = Github(base_url="https://api.github.com", login_or_token="access_token")
#
#
# # for repo in g.get_user().get_repos():
# #     print(repo.name)
# #     repo.edit(has_wiki=False)
# #     # to see all the available attributes and methods
# #     print(dir(repo))
#
# gh = Github("amirarcane", "secretof1993")
# repo = gh.get_repo('tensorflow/tensorflow')
# counter = 0
# for pull in repo.get_pulls(state='all'):
#     counter += 1
#     print(pull.get)
#
# print(counter)


# from datetime import datetime
import csv
import time
import traceback
# import os
import requests
import json

pageCount = 121
result = []
result2 = []


csv_file = ".csv"
csv_columns = ['id', 'title', 'url', 'node_id', 'html_url', 'diff_url', 'patch_url','issue_url', 'number', 'state',
               'locked','title', 'user', 'body', 'created_at', 'updated_at','closed_at', 'merged_at', 'merge_commit_sha',
               'assignee', 'assignees', 'requested_reviewers', 'requested_teams', 'labels', 'milestone', 'commits_url',
               'review_comments_url', 'review_comment_url', 'comments_url', 'statuses_url', 'head', 'base', '_links',
               'author_association']


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
        path = 'not merged.csv'
        with open(path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for dict in result:
                # for data in dict:
                writer.writerow(dict)
    except:
        traceback.print_exc()
        print(str)


url = "https://api.github.com/repos/tensorflow/tensorflow/pulls?state=all&per_page=100&page="

try:
    while pageCount < 127:
        response = json.loads(requests.get(url + str(pageCount)).text)

        if len(response) == 1:
            print('limit reached!')
            break

        print(pageCount)

        for item in response:
            if item['state'] == 'closed' and item['merged_at'] is None:
                result.append(item)
                # writeToFile(item)



        pageCount += 1
        # time.sleep(1)

    for i in range(0, len(result)):
        if result[i] not in result[i + 1:]:
            result2.append(result[i])
    writeToFile(result2)
except Exception:
    for i in range(0, len(result)):
        if result[i] not in result[i + 1:]:
            result2.append(result[i])
    writeToFile(result2)
    traceback.print_exc()

# writeToFile()

