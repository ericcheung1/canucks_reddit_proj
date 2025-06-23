import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.sentiment_utils.vader_sentiment_utils import flatten_list, calculate_vader_scores
import pytest


def test_calculate_vader_scores_with_comments(mock_post_with_comments, vader_sia):
    score_dict = calculate_vader_scores(mock_post_with_comments, vader_sia)

    assert score_dict["Total_Comments"] == 5

def test_calculate_vader_scores_with_blanks(mock_post_with_blank_comments, vader_sia):
    score_dict = calculate_vader_scores(mock_post_with_blank_comments, vader_sia)

    assert score_dict["Total_Comments"] == 0
    assert score_dict["Total_Neg"] == 0
    assert score_dict["Total_Neu"] == 0
    assert score_dict["Total_Pos"] == 0

def test_calculate_vader_scores_with_deleted(mock_post_with_deleted_comments, vader_sia):
    score_dict = calculate_vader_scores(mock_post_with_deleted_comments, vader_sia)

    assert score_dict["Total_Comments"] == 0
    assert score_dict["Average_Neg"] == 0.0
    assert score_dict["Average_Neu"] == 0.0
    assert score_dict["Average_Pos"] == 0.0
    assert score_dict["Average_Compound"] == 0.0

def test_flatten_list_with_comment(mock_post_with_comments):
    flattened_list = flatten_list(mock_post_with_comments)

    assert len(flattened_list) == 5

def test_flatten_list_with_blanks(mock_post_with_blank_comments):
    flattened_list = flatten_list(mock_post_with_blank_comments)

    assert len(flattened_list) == 0

def test_flatten_list_with_deleted(mock_post_with_deleted_comments):
    flattened_list = flatten_list(mock_post_with_deleted_comments)

    assert len(flattened_list) == 0