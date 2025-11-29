import pandas as pd
from datetime import datetime
import os

def format_timestamp(timestamp):
    """Convert Unix timestamp to readable date format."""
    try:
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return timestamp

def format_genres(genres):
    """Convert pipe-delimited genres to comma-separated format."""
    if pd.isna(genres):
        return genres
    return genres.replace('|', ', ')

def calculate_average_ratings(ratings_df):
    """Calculate average rating and count for each movie."""
    avg_ratings = ratings_df.groupby('movieId')['rating'].agg(['mean', 'count']).reset_index()
    avg_ratings.columns = ['movieId', 'avg_rating', 'rating_count']
    return avg_ratings

def merge_movies_with_ratings(movies_df, avg_ratings):
    """Merge movies with their average ratings."""
    movies_with_ratings = movies_df.merge(avg_ratings, on='movieId', how='left')
    movies_with_ratings['avg_rating'] = movies_with_ratings['avg_rating'].fillna(0)
    movies_with_ratings['rating_count'] = movies_with_ratings['rating_count'].fillna(0)
    return movies_with_ratings

def load_data():
    """Load and prepare all movie data."""
    # Use relative paths from the working directory (/app)
    movies_path = 'assets/ml-latest-small/movies.csv'
    ratings_path = 'assets/ml-latest-small/ratings.csv'
    
    movies_df = pd.read_csv(movies_path)
    ratings_df = pd.read_csv(ratings_path)
    
    # Format timestamps in the ratings dataframe
    ratings_df['timestamp'] = ratings_df['timestamp'].apply(format_timestamp)
    
    # Format genres to be comma-separated
    movies_df['genres'] = movies_df['genres'].apply(format_genres)
    
    avg_ratings = calculate_average_ratings(ratings_df)
    movies_with_ratings = merge_movies_with_ratings(movies_df, avg_ratings)
    
    return movies_df, ratings_df, movies_with_ratings
