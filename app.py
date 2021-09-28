from flask import Flask, jsonify, request
import csv 

app = Flask(__name__)

allMovies = []
likedMovies = []
dislikedMovies = []
notWatchedMovies = []

with open("movies.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    



@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })
allMovies = allMovies
@app.route("/liked-movie",methods = ["POST"])
def liked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-movie",methods = ["POST"])
def disliked_movies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    dislikedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-watched-movies",methods = ["POST"])
def notWatchedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    notWatchedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run(debug=True)

