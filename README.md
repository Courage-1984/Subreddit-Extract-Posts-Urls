# Subreddit-Extract-Posts-Urls
Extract Subreddit Posts' Urls

# Steps
First Download the script `subreddit_extract_post_urls.py` in the above repository.
1. Navigate to:
``` sh
  https://old.reddit.com/prefs/apps/
```
2. Click the "are you a developer? create an app..." button or the "create another app..." button and fill out the form like so:
      * choose a name
      * select "web app"
      * set ``http://localhost:6414/`` as "redirect uri"
      * solve the "I'm not a rebot" reCATCHA if needed
      * click "create app"
3. Copy the client id (third line, underneath your application's name and "web app") and put it in the downloaded .py script you downloaded earlier as the ``"your_client_id"``.
4. Copy the secret value and put it in the downloaded .py script you downloaded earlier as the ``"your_client_secret"``.
5. In your downloaded .py script use "``Python:<application name>:v1.0 (by /u/<username>)``" as ``user_agent`` and replace ``<application name>`` and ``<username>`` accordingly.
6. In your downloaded .py script replace `subreddit_name` with the subreddit from which you would like to get the posts' urls from (without the `r/`).
7. Run the script using the following in your terminal:
``` sh
  python subreddit_extract_post_urls.py
```

Ta-da!
