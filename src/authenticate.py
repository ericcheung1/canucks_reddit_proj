import configparser
import praw
import os

def authenticate_reddit(config_file):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config = configparser.ConfigParser()
    config.read(os.path.join(project_root, config_file))
    reddit_instance = praw.Reddit(
        client_id=config.get('reddit', 'client_id'),
        client_secret=config.get('reddit', 'client_secret'),
        username=config.get('reddit', 'username'),
        password=config.get('reddit', 'password'),
        user_agent="test_bot"
        )
    
    print(f'Logged in as user: {reddit_instance.user.me()}')
    return reddit_instance

