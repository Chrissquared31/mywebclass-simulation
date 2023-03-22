import requests
import datetime

# Replace with your own values
owner = 'Chrissquared31'
repo = 'mywebclass-simulation'
access_token = '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'

# API endpoint for getting commits
url = f'https://api.github.com/repos/{owner}/{repo}/commits'

# Set headers and authentication
headers = {'Authorization': f'token {access_token}'}
params = {'per_page': 100}

# Send GET requests to the API endpoint
commits = []
while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if not data:
        break
    commits.extend(data)
    params['page'] = params.get('page', 1) + 1

# Create a log file
with open(f'{repo}-log.txt', 'w') as f:
    f.write(f'Commit log for {repo}\n\n')
    for commit in commits:
        date = datetime.datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
        date_str = date.strftime('%Y-%m-%d %H:%M:%S')
        author = commit['commit']['author']['name']
        message = commit['commit']['message'].strip()
        f.write(f'{date_str} - {author}: {message}\n')