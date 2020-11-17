from flask import Flask,jsonify,request
import csv

allmovies = []
with open('movies.csv')as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

liked_movies = []
did_not_watched = []
unliked_movies = []

app = Flask(__name__)
@app.route("/get-movies")
def get_movie():
    return jsonify({
        "data":allmovies[0],
        "status":"success"
    })
@app.route("/liked_movies",methods = ["POST"])
def likedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"

    }),201

@app.route("/unliked_movies",methods = ["POST"])
def unlikedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did_not_watched",methods = ["POST"])
def didNotWatched():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    did_not_watched.append(movie)
    return jsonify({
        "status":"success"
    }),201


if __name__ == "__main__":
    app.run()
