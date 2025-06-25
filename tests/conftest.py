import pytest
from transformers import pipeline # type: ignore
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Mock_Post():
    def __init__(self, post_id, comments=None):
        self.title = post_id
        self.comments = comments if comments is not None else []

class Mock_Comment():
    def __init__(self, body, comment_id, replies=None):
        self.body = body
        self.replies = replies if replies is not None else []
        self.comment_id = comment_id

@pytest.fixture
def mock_post_with_comments():
    reply_1_1 = Mock_Comment(body="I love the Vancouver Canucks!", replies=[], comment_id="abc12")
    reply_2_1 = Mock_Comment(body="I hate the the Canucks!", replies=[], comment_id="h12bb4")
    comment_1 = Mock_Comment(body="Wow what an amazing game", replies=[reply_1_1, reply_2_1], comment_id="j1j4h")

    reply_2_1 = Mock_Comment(body="Totally agree with that!", replies=[], comment_id="jg3g1")
    comment_2 = Mock_Comment(body="This game was terrible", replies=[reply_2_1], comment_id="h5h3b")

    post = Mock_Post(post_id="123abc", comments=[comment_1, comment_2])

    return post

@pytest.fixture
def mock_post_with_blank_comments():
    post = Mock_Post(post_id="456def", comments=[])

    return post

@pytest.fixture
def mock_post_with_deleted_comments():
    comment_1 = Mock_Comment(body="[deleted]", replies=[], comment_id="hh4h3")
    comment_2 = Mock_Comment(body="[deleted]", replies=[Mock_Comment(body="[deleted]", replies=[], comment_id="g3g1h")], comment_id="1h1j2")
    post = Mock_Post(post_id="dfd232", comments=[comment_1, comment_2])

    return post

@pytest.fixture
def distilbert_pipeline():
    return pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@pytest.fixture
def vader_sia():
    return SentimentIntensityAnalyzer()