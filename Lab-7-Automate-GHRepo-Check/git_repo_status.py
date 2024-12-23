import requests
from datetime import datetime, timedelta

GITHUB_TOKEN = 'ghp_xxxxxxxxxxxxxxxxxxxxxx'
GITHUB_USERNAME = 'mayanktripathi4u'
GITHUB_API_URL = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'

# Set headers with token for authentication.
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

# Calculate 30 Days delta
days = 30
current_date = datetime.now()
thirty_days_ago = current_date - timedelta(days=days)
print(f"Will look the activity for past {days} days, ie from {thirty_days_ago} to {current_date}.")

def get_repos_not_modified_in_last_x_days():
    # Use resuests library to send an HTTP GET request to the specified GH API with header.
    response = requests.get(GITHUB_API_URL, headers=headers)

    # Check if the request was success
    if response.status_code == 200:
        # Convert API Response to JSON.
        repos = response.json()
        inactive_repos = []

        # Iterate over the repos
        for repo in repos:
            last_modified = datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
            print("Last Modified Date Time", last_modified)
            
            if last_modified < thirty_days_ago :
                inactive_repos.append(repo['name'])


        if inactive_repos:
            print("Below Repo is not used or modified in last {days} days.")
            for repo_name in inactive_repos:
                print(f"  - {repo_name}")
        else:
            print("All repos have been modified in the last {days} days.")
        
    else:
        print("Failed to retrieve repostories : {response.status_code}")


# Run the Function
get_repos_not_modified_in_last_x_days()

