import os
from authenticate import authenticate_reddit
import praw
from datetime import datetime as dt, timedelta, timezone
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)

reddit_instance = authenticate_reddit('config.ini')

game_log = pd.read_csv(os.path.join(project_root, 'data', 'formatted_van_schedule24_25.csv'))
subreddit = reddit_instance.subreddit('canucks')

game_log['UTC_Timestamp'] = pd.to_datetime(game_log['UTC_Timestamp'])
relavent_results = []
relavent_ids = set()
for index, game in game_log.iterrows():
    query = f'Post Game Thread: {game['Opponent']} {game['Day']} {game['Month']} {game['Year']}'
    results = subreddit.search(query=query, sort='relavent', time_filter='all')
    game_end_utc = pd.to_datetime(game['UTC_Timestamp']) + timedelta(hours=4)
    for submission in results:
        submission_time_utc = dt.fromtimestamp(submission.created_utc, timezone.utc)
        title_format = (submission.title.__contains__(f'Post Game Thread: {game['Opponent']} at Vancouver Canucks') or
                        submission.title.__contains__(f'Post Game Thread: Vancouver Canucks at {game['Opponent']}'))
        if submission.id not in relavent_ids and (submission_time_utc <= game_end_utc and title_format):
            print(submission.title)
            relavent_results.append(submission)
            relavent_ids.add(submission.id)

print(len(relavent_results))
