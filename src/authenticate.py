import configparser
import praw
import os

def authenticate_reddit(config_file):
    """
    Authenticates a reddit instance in PRAW.

    Authenticates a reddit instance using 
    information and keys from a config file.

    Args:
        config_file (.ini file): Config file contain keys and information.

    Returns:
        reddit_instance (praw.Reddit): A praw reddit instance.
    """
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

