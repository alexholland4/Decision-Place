# Decision Simplifier 🧠

A web-based tool that helps users make decisions by presenting pairwise comparisons rather than overwhelming them with too many options at once. Inspired by the Paradox of Choice, the tool helps users rank items (e.g., ideas, priorities, products) by selecting between pairs. The end result is a sorted list based on their preferences — derived intuitively and with reduced cognitive load.

## Project Overview

This tool implements a pairwise comparison system to help users rank a list of items. Users input their items, then iteratively choose their preference between two items at a time. The system then calculates and presents a ranked list.

## Core Features Implemented

* **Intro Section**: Brief summary of the Paradox of Choice.
* **User Input**: Users can enter 5–15 items.
* **Pairwise Comparison Engine**: System generates unique pairwise matchups and presents them one at a time.
* **Ranking Result**: Displays the ranked list based on user choices.
* **Restart**: Option to clear session and start over.

## Technical Specifications

* **Frontend**: HTML, CSS, JavaScript (Vanilla)
* **Backend**: Python + Flask
* **Ranking Logic**: Based on win counts from pairwise comparisons.

## Running the Application
1.  Ensure Python and Flask are installed (`pip install Flask`).
2.  Navigate to the `decision-simplifier` directory.
3.  Run the Flask application: `python app.py`
4.  Open your web browser and go to `http://127.0.0.1:5000`.