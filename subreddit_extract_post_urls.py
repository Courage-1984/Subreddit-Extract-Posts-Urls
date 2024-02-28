import praw

# replace with your own Reddit API credentials
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='Python:<application name>:v1.0 (by /u/<username>)')

subreddit = reddit.subreddit('subreddit_name')

links = []

submission_generator = subreddit.new(limit=None)

for submission in submission_generator:
    links.append(submission.url)

with open('links.txt', 'w') as f:
    for link in links:
        f.write(f'{link}\n')

print(f'Saved {len(links)} links to links.txt')
