import praw

# replace with your own Reddit API credentials
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='Python:<application name>:v1.0 (by /u/<username>)')

subreddit = reddit.subreddit('liminalpools')

links = []

after = None

while True:
    submissions = subreddit.new(limit=100, params={'after': after})
    
    if not submissions:
        break

    for submission in submissions:
        links.append(submission.url)
        with open('links.txt', 'a') as f:
            f.write(f'{submission.url}\n')

    after = submission.id
    print(f'Fetched {len(links)} links so far...')

print(f'Saved {len(links)} links to links.txt')
