import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.sentiment_utils.distilBERT_sentiment_utils import calculate_distilbert_scores, flatten_list
import pytest

# def test_calc_distilber_scores_with_comments(mock_post_with_comments, distilbert_pipeline):
#     score_dict = calculate_distilbert_scores(mock_post_with_comments, distilbert_pipeline)

#     assert len(score_dict["sentiment_label"]) == 5
#     assert score_dict["confidence_score"][0] > 0.80

def test_flatten_list_with_comments(mock_post_with_comments, distilbert_pipeline):
    all_text_bodies = flatten_list(mock_post_with_comments)

    assert all_text_bodies[0]["comment_id"] == "j1j4h"