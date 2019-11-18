import pandas as pd
import re


# open csvs
all_commits = pd.read_csv("commits.csv", header=0)
all_pull_req = pd.read_csv("PRs-h1.csv", header=0)

all_keywords = ["close", "closes", "closed", "fix", "fixes", "fixed", "resolve", "resolves", "resolved","merge","merges","merged"]

find_results = []

for index, commit in all_commits.iterrows():
    commit_message = str(commit[1]).lower()

    if any(keyword in commit_message for keyword in all_keywords):
        hashtags = re.findall(r"#(\w+)", commit_message)

        if len(hashtags) != 0:
            try:
                pull_req_num = int(hashtags[0])
            except:
                continue

            row = all_pull_req.loc[all_pull_req['number'] == pull_req_num]
            if row.empty:
                pass
            else:
                all_pull_req = all_pull_req.drop(row.index[0])
                find_results.append(list(row.iloc[0]))

                print("ok")


all_pull_req.to_csv("h2_PRs.csv", header=True, index= None)
h2_out = pd.DataFrame(find_results, columns=["id","title","url","node_id","html_url","diff_url","patch_url","issue_url","number","state","locked","title","user","body","created_at","updated_at","closed_at","merged_at","merge_commit_sha","assignee","assignees","requested_reviewers","requested_teams","labels","milestone","commits_url","review_comments_url","review_comment_url","comments_url","statuses_url","head","base","_links","author_association"])
h2_out.to_csv("h2_out.csv", header=True, index=None)
