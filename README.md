# MovieLens Explorer

A containerized Flask web application for exploring movie ratings and generating genre-based recommendations using the MovieLens dataset.

## 1) Executive Summary

**Problem:** Movie enthusiasts and data analysts need an easy way to explore movie ratings, understand rating distributions, and discover similar movies based on genre preferences without writing complex queries or data processing scripts.

**Solution:** MovieLens Explorer is a web-based application that provides an intuitive interface to browse popular movies, view detailed rating statistics, and get personalized recommendations based on genre similarity. The application processes 100,000+ ratings across 9,000+ movies and presents the data through clean HTML interfaces and RESTful API endpoints.

## 2) System Overview

### Course Concepts

This project demonstrates the following DS 2022 concepts:

- **Week 7: Containers in Production** - Docker containerization for reproducible deployment
- **Week 8: Serving APIs** - Flask REST API for data serving
- **Week 3: Scripting Pipelines** - Automated data transformation and loading

### Architecture

![System Architecture](assets/architecture.png)

The application follows a three-tier architecture:

1. **Data Layer**: CSV files from MovieLens dataset (movies, ratings)
2. **Processing Layer**: Python pandas for data transformation and aggregation
3. **Presentation Layer**: Flask web server with HTML templates and REST API endpoints

### Data Sources

- **Dataset**: MovieLens Latest Small Dataset
- **Source**: [GroupLens Research](https://grouplens.org/datasets/movielens/)
- **Size**: 100,836 ratings, 9,742 movies
- **Format**: CSV files (movies.csv, ratings.csv)
- **License**: Available for education and research purposes
- **Citation**: F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19.

## 3) How to Run (Local)

### Prerequisites

- Docker installed on your system
- Port 5000 available

### Quick Start (One Command)

```bash
./run.sh

### This script will:

1. Build the Docker image
2. Stop any existing container
3. Start the application
4. Run Tests
5. Display access information

### Manual Docker Commands
# Build the image
docker build -t movielens-api:latest .

# Run the container
docker run -d --name movielens-api -p 5000:5000 movielens-api:latest

# Check if running
curl http://localhost:5000/

### Access the Application
- Web Interface: http://localhost:5000
- API Endpoints:
    - GET / - Home page with statistics
    - GET /movies - Browse popular movies
    - GET /movie/<id> - View specific movie details
    - GET /recommend/<id> - Get movie recommendations
    - GET /api/movies - JSON API for movies list
    - GET /api/movie/<id> - JSON API for movie details

### Stop the Application
``
docker stop movielens-api
docker rm movielens-api
``

# Tests

## Running Tests

Start the application:
```bash
./run.sh


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MovieLens dataset provided by GroupLens Research
- Course: DS 2022 - Systems I: Intro to Computing
- University of Virginia School of Data Science

## Citation

If you use this project or the MovieLens dataset, please cite:


## Project Structure
``
carolinsis/
├── src/
│ ├── app.py # Flask application and routes
│ ├── data_management.py # Data loading and processing
│ ├── templates/ # HTML templates
│ │ ├── home.html
│ │ ├── movies.html
│ │ ├── movie.html
│ │ ├── recommendations.html
│ │ └── error.html
│ └── static/ # CSS stylesheets
│ └── style.css
├── assets/
│ └── ml-latest-small/ # MovieLens dataset
│ ├── movies.csv
│ ├── ratings.csv
│ ├── links.csv
│ └── tags.csv
├── Dockerfile # Container definition
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── run.sh # One-command launcher
├── LICENSE # MIT License
└── README.md # This file
``

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MovieLens dataset provided by GroupLens Research
- Course: DS 2022 - Systems I: Intro to Computing
- University of Virginia School of Data Science

## Citation

If you use this project or the MovieLens dataset, please cite:



## Running Locally (Without Docker)

If you prefer to run the application directly on your machine without Docker:

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Run the Application
python src/app.py

## Deactivate Virtual Environment
When you're done:
deactivate
