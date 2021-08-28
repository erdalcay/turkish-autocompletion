import sys
import pickle
sys.path.insert(0, "..")
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from lib.levenshtein import min_edit_distance


with open("./src/corpus.pickle", "rb") as file:
    corpus = pickle.load(file)

app = Flask(__name__)
CORS(app)

@app.route("/suggestions", methods=["POST"])
@cross_origin()
def get_suggestions():
    MAX_RESULTS = 10

    data = request.json
    if not data or "prefix" not in data:
        return jsonify([])

    prefix = data["prefix"]
    suggested_words = corpus.suggest_words(prefix.lower())
    if not suggested_words:
        return jsonify([])

    suggested_words.sort(key=lambda word: min_edit_distance(word, prefix))
    return jsonify(suggested_words[:MAX_RESULTS])

@app.errorhandler(500)
@app.errorhandler(405)
@app.errorhandler(404)
def error_handler(_):
    return make_response("Not Found", 404)
