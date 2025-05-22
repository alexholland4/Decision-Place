# Decision Place

Overwhelmed by too many options? The "Paradox of Choice" suggests that while we might believe more choices are better, having too many can actually lead to decision paralysis and dissatisfaction. Inspired by research on behavior science and decision-making, this web-based tool that helps users make decisions by presenting pairwise comparisons rather than overwhelming them with too many options at once.

Try it out at (https://decision-place.onrender.com/)

## Project Overview

This tool implements a pairwise comparison system to help users rank a list of items. Users input their items, then iteratively choose their preference between two items at a time. The system then calculates and presents a ranked list.

## Core Features Implemented

* **Intro Section**: Brief summary of the Paradox of Choice.
* **User Input**: Users enters items (usually 5-15).
* **Pairwise Comparison Engine**: System dynamically generates unique pairwise matchups and presents them one at a time.
* **Ranking Result**: Displays the ranked list based on user choices.
* **Restart**: Option to clear session and start over.

## Technical Specifications

* **Frontend**: HTML, CSS, JavaScript (Vanilla)
* **Backend**: Python + Flask
* **Ranking Logic**: Based on win counts from pairwise comparisons.

## Try It Yourself!

Use this project any time at (https://decision-place.onrender.com/)
