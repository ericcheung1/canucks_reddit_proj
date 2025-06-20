# Canucks Fan Sentiment Analysis (Ongoing)

Live Demo: https://canucks-sentiment.onrender.com (Initial load may take a minute; homepage content is still in development)

## Project Overview

This project is an ongoing effort to analyze the sentiment of Vancouver Canucks fans regarding the 2024-25 NHL season by examining post-game discussions on Reddit. It encompasses data collection, web application development for data display, sentiment analysis and future player mention tracking.

The completed phase involved:
* Gathering comments and replies from post-game threads within the r/canucks subreddit using the PRAW API.
* Implementing VADER-based sentiment scoring.
* Building and deploying a Flask-based web application to display this content.
* Migrating the database to MongoDB Atlas for cloud access.

The current phase involves:
* Initiating the implementation of sentiment analysis using Machine Learning (ML) -based models.

## Data Collection

Data is collected from the following sources:

* **Reddit API:** Utilizing the PRAW (Python Reddit API Wrapper) library to access and retrieve comments from the r/canucks subreddit.
* **Subreddit:** r/canucks (https://www.reddit.com/r/canucks/) - Specifically targeting post-game threads for the 2024-25 season.

The scripts responsible for data collection is with the `src/reddit_pipeline/` folder

## Web Application

A Flask web application has been developed and deployed to present the collected Reddit posts and comments.

* **Display:** Each Reddit post and its associated comments/replies are viewable on the web interface.
* **Frontend:** Built using basic HTML. CSS integration is in progress.
* **Backend:** Powered by Flask.
* **Sentiment Analysis:** VADER-based sentiment scores are computed for individual comments.
* **Database:** MongoDB Atlas used for remote data storage and retrieval.
* **Object-Document Mapper (ODM):** MongoEngine is used for database schema and interactions.

## Technologies Used

* **Python:** The primary programming language.
* **PRAW (Python Reddit API Wrapper):** For interacting with the Reddit API.
* **Flask:** Web framework for building the application.
* **MongoDB Atlas** The cloud-hosted version of MongoDB.
* **MongoEngine:** Python Object-Document Mapper (ODM) for MongoDB, used for defining and interacting with data schemas.
* **PyMongo:** The official MongoDB driver for Python, handling direct database operations.
* **HTML:** For the web application's frontend structure.
* **CSS:** For the web application's styling.
* **NLTK (Natural Language Toolkit):** Specifically VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis.

## Future Enhancements

Planned next steps and potential features for this project include:

* **BERT Integration:** Fine-tune and integrate a custom transformer-based model to improve sentiment classification.
* **Player Mention Tracking:** Identifying and tracking mentions of specific players within the comments.
* **Homepage/About Section:** Add project context, methodology, and explanation of analysis choices.
* **"All Posts" View:** Polish the overview page which currently lists each post with titles and links.
* **CI/CD Integration:** Set up GitHub Actions for automated deployment and testing.
