# Canucks Fan Sentiment Analysis (Ongoing)

## Project Overview

This project is an ongoing effort to analyze the sentiment of Vancouver Canucks fans regarding the 2024-25 NHL season by examining post-game discussions on Reddit. It encompasses data collection, web application development for data display, and future sentiment analysis.

The completed phase involved:
* Gathering comments and replies from post-game threads within the r/canucks subreddit using the PRAW API.

The current phase involves:
* A Flask-based web application that displays these collected Reddit posts, along with all their associated comments and replies.
* Initiating the implementation of sentiment analysis using NLTK's VADER.

## Data Collection

Data is collected from the following sources:

* **Reddit API:** Utilizing the PRAW (Python Reddit API Wrapper) library to access and retrieve comments from the r/canucks subreddit.
* **Subreddit:** r/canucks (https://www.reddit.com/r/canucks/) - Specifically targeting post-game threads for the 2024-25 season.

The scripts responsible for data collection is with the src/reddit_pipeline/ folder

## Web Application

A Flask web application has been developed to present the collected Reddit posts and comments.

* **Display:** Each Reddit post and its associated comments/replies are displayed on the web interface.
* **Frontend:** Currently utilizes basic HTML for presentation.
* **Backend:** Powered by Flask.
* **Object-Document Mapper (ODM):** MongoEngine is used for interacting with the database.

## Technologies Used

* **Python:** The primary programming language.
* **PRAW (Python Reddit API Wrapper):** For interacting with the Reddit API.
* **Flask:** Web framework for building the application.
* **MongoEngine:** Python Object-Document Mapper (ODM) for MongoDB.
* **HTML:** For the web application's frontend structure.
* **NLTK (Natural Language Toolkit):** Specifically VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis (currently in progress).

## Future Enhancements

Planned next steps and potential features for this project include:

* **Sentiment Score Display:** Integrating and displaying the calculated sentiment scores for each comment/post in the web application.
* **Player Mention Tracking:** Identifying and tracking mentions of specific players within the comments.
* **Styling (CSS):** Separating styling from HTML into dedicated CSS files for improved maintainability and aesthetics.
