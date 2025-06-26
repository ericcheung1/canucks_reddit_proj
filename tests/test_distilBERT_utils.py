import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.sentiment_utils.distilBERT_sentiment_utils import calculate_distilbert_scores, flatten_list
import pytest

def test_calc_distilbert_with_comments(mock_post_with_comments, distilbert_pipeline):
    score_dict = calculate_distilbert_scores(mock_post_with_comments, distilbert_pipeline)

    assert len(score_dict["sentiment_label"]) == 5
    assert score_dict["confidence_score"][0] > 0.80
    assert score_dict["comment_id"][0] == "j1j4h"
    assert score_dict["comment_id"][1] == "abc12"
    assert score_dict["comment_id"][2] == "h12bb4"
    assert score_dict["comment_id"][3] == "h5h3b"
    assert score_dict["comment_id"][4] == "jg3g1"

def test_calc_distilbert_with_blanks(mock_post_with_blank_comments, distilbert_pipeline):
    score_dict = calculate_distilbert_scores(mock_post_with_blank_comments, distilbert_pipeline)

    assert len(score_dict["sentiment_label"]) == 0
    assert score_dict["confidence_score"] == []
    assert score_dict["comment_id"] == []

def test_calc_distilbert_with_deleted(mock_post_with_deleted_comments, distilbert_pipeline):
    score_dict = calculate_distilbert_scores(mock_post_with_deleted_comments, distilbert_pipeline)

    assert len(score_dict["sentiment_label"]) == 0
    assert score_dict["confidence_score"] == []
    assert score_dict["comment_id"] == []

def test_flatten_list_with_comments(mock_post_with_comments):
    all_text_bodies = flatten_list(mock_post_with_comments)

    assert all_text_bodies[0]["comment_id"] == "j1j4h"
    assert all_text_bodies[1]["comment_id"] == "abc12"
    assert all_text_bodies[2]["comment_id"] == "h12bb4"
    assert all_text_bodies[3]["comment_id"] == "h5h3b"
    assert all_text_bodies[4]["comment_id"] == "jg3g1"
    assert all_text_bodies[0]["body"] == "Wow what an amazing game"
    assert all_text_bodies[1]["body"] == "I love the Vancouver Canucks!"
    assert all_text_bodies[2]["body"] == "I hate the the Canucks!"
    assert all_text_bodies[3]["body"] == "This game was terrible"
    assert all_text_bodies[4]["body"] == "Totally agree with that!"

def test_flatten_list_with_blank_comments(mock_post_with_blank_comments):
    all_text_bodies = flatten_list(mock_post_with_blank_comments)

    assert all_text_bodies == []

def test_flatten_list_with_with_deleted_comments(mock_post_with_deleted_comments):
    all_text_bodies = flatten_list(mock_post_with_deleted_comments)

    assert all_text_bodies == []
