from flask import Flask, render_template, jsonify, request
import pandas as pd
from data_management import load_data

app = Flask(__name__)

# Load data once at startup
movies_df, ratings_df, movies_with_ratings = load_data()

@app.route('/')
def home():
    return render_template('home.html', 
                         total_movies=len(movies_df),
                         total_ratings=len(ratings_df))

@app.route('/movies')
def movies_page():
    limit = request.args.get('limit', default=50, type=int)
    popular_movies = movies_with_ratings.sort_values('rating_count', ascending=False).head(limit)
    movies = popular_movies.to_dict('records')
    return render_template('movies.html', movies=movies, count=len(movies))

@app.route('/movie/<int:movie_id>')
def movie_page(movie_id):
    movie = movies_with_ratings[movies_with_ratings['movieId'] == movie_id]
    
    if movie.empty:
        return render_template('error.html', error="Movie not found"), 404
    
    movie_data = movie.iloc[0].to_dict()
    movie_ratings = ratings_df[ratings_df['movieId'] == movie_id].head(5)
    sample_ratings = movie_ratings.to_dict('records')
    
    return render_template('movie.html', 
                         movie=movie_data, 
                         sample_ratings=sample_ratings)

@app.route('/recommend/<int:movie_id>')
def recommend_page(movie_id):
    source_movie = movies_with_ratings[movies_with_ratings['movieId'] == movie_id]
    
    if source_movie.empty:
        return render_template('error.html', error="Movie not found"), 404
    
    source_genres = source_movie.iloc[0]['genres']
    source_title = source_movie.iloc[0]['title']
    genre_list = source_genres.split('|')
    
    def genre_match_score(genres):
        if pd.isna(genres):
            return 0
        movie_genres = set(genres.split('|'))
        source_genres_set = set(genre_list)
        return len(movie_genres.intersection(source_genres_set))
    
    movies_with_ratings['match_score'] = movies_with_ratings['genres'].apply(genre_match_score)
    
    recommendations = movies_with_ratings[
        (movies_with_ratings['movieId'] != movie_id) & 
        (movies_with_ratings['rating_count'] >= 10) &
        (movies_with_ratings['match_score'] > 0)
    ].sort_values(['match_score', 'avg_rating'], ascending=[False, False]).head(10)
    
    recs = recommendations.to_dict('records')
    
    return render_template('recommendations.html',
                         source_movie={'id': movie_id, 'title': source_title, 'genres': source_genres},
                         recommendations=recs)

# API endpoints (keep for backwards compatibility)
@app.route('/api/movies')
def api_movies():
    limit = request.args.get('limit', default=50, type=int)
    popular_movies = movies_with_ratings.sort_values('rating_count', ascending=False).head(limit)
    result = popular_movies[['movieId', 'title', 'genres', 'avg_rating', 'rating_count']].to_dict('records')
    return jsonify({"count": len(result), "movies": result})

@app.route('/api/movie/<int:movie_id>')
def api_movie(movie_id):
    movie = movies_with_ratings[movies_with_ratings['movieId'] == movie_id]
    if movie.empty:
        return jsonify({"error": "Movie not found"}), 404
    movie_data = movie.iloc[0].to_dict()
    return jsonify({"movie": movie_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
