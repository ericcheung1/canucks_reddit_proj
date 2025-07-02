# Canucks Sentiment Analysis (Ongoing)

Live Site: https://canucks-sentiment.onrender.com (Initial load may take up to a minute)

## Project Overview

This project is an ongoing effort to analyze the sentiment of Vancouver Canucks fans regarding the 2024-25 NHL season by examining post-game discussions on Reddit. It encompasses data collection, sentiment analysis, and web application development for data display

The completed phase involved:
* Gathering comments and replies from post-game threads within the r/canucks subreddit using the PRAW API.
* Implementing VADER-based and BERT-based sentiment scoring.
* Deploying a MongoDB Atlas database for cloud access.
* Building and deploying a Flask-based web application to display this content.

## Data Collection

Data is collected from the following sources:

* **Reddit API:** Utilizing the PRAW (Python Reddit API Wrapper) library to access and retrieve comments from the r/canucks subreddit.
* **Subreddit:** r/canucks (https://www.reddit.com/r/canucks/) - Specifically targeting post-game threads for the 2024-25 NHL season.

The utility scripts responsible for data collection is with the `src/reddit_pipeline/` folder and the main script is `src/main_pipeline.py`

## Web Application

A Flask web application has been developed and deployed to present the collected Reddit posts and comments along with the sentiment analysis results.

* **Display:** Each Reddit post, its associated comments/replies, and sentiment analysis results are viewable on the web interface.
* **Frontend:** Made using basic HTML and CSS.
* **Backend:** Powered by Flask.
* **Sentiment Analysis:** VADER-based and BERT-based sentiment scores are computed for every post-game thread and every individual comment.
* **Database:** MongoDB Atlas used for remote data storage and retrieval.
* **Object-Document Mapper (ODM):** MongoEngine is used for database schema and interactions.

## Technologies Used

* **Python:** The primary programming language.
* **PRAW (Python Reddit API Wrapper):** For interacting with the Reddit API.
* **Flask:** Web framework for building the application.
* **MongoDB Atlas** The cloud-hosted version of MongoDB used for remote access.
* **MongoEngine:** Python Object-Document Mapper (ODM) for MongoDB, used for defining and interacting with data schemas.
* **PyMongo:** The official MongoDB driver for Python, handling direct database operations.
* **HTML & CSS:** For the web application's frontend structure and styling.
* **NLTK (Natural Language Toolkit):** Specifically VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis.
* **BERT (Bidirectional Encoder Representations from Transformers):** DistilBERT a lighter, more efficient variant of BERT for sentiment analysis.

## Future Enhancements

Planned next steps and potential features for this project include:

* **Sentiment Visualization:** Graph VADER and DistilBERT results from throughout the 2024-25 NHL season.
* **Player Mention Tracking:** Identifying and tracking mentions of specific players within the comments.
* **CI/CD Integration:** Set up GitHub Actions for automated deployment and testing.
