# 6/16/2025
# Adam Alberski
# GitHub user activity
# http://roadmap.sh/projects/github-user-activity

import sys
import requests
from collections import defaultdict

def main(username):

    response = requests.get('https://api.github.com/users/' + username + '/events')

    if response.status_code == 200:

        summary = defaultdict(int)

        for event in response.json():
            match event['type']:
                case 'PushEvent':
                    key = f"Pushed to {event['repo']['name']}"
                case 'CreateEvent':
                    key = f"Created {event['repo']['name']}"
                case 'PullRequestEvent':
                    key = f"Created pull request {event['payload']['pull_request']['number']}"
                case 'PullRequestReviewEvent':
                    key = f"Reviewed pull request {event['payload']['pull_request']['number']}"
                case 'PullRequestCommentEvent':
                    key = f"Commented on pull request {event['payload']['pull_request']['number']}"
                case 'IssueCommentEvent':
                    key = f"Commented on issue {event['payload']['issue']['number']}"
                case 'IssuesEvent':
                    key = f"Created issue {event['payload']['issue']['number']}"
                case 'WatchEvent:':
                    key = f"Starred {event['payload']['issue']['number']}"
            summary[key] += 1

        print(f"\nSummary for {username}:\n")
        for action, count in summary.items():
            if count == 1:
                print(f"{action}")
            else:
                print(f"{action} {count} times")
        print()
    else:
        print(response.status_code)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a GitHub username as a command line argument.")