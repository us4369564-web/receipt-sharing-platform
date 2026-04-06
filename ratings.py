from flask import Blueprint, request, jsonify

ratings = Blueprint('ratings', __name__)

recipe_ratings = {}
favorites = {}

@ratings.route('/rate/<int:recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
    data = request.json
    score = data.get("score", 0)

    if recipe_id not in recipe_ratings:
        recipe_ratings[recipe_id] = []

    recipe_ratings[recipe_id].append(score)

    avg = sum(recipe_ratings[recipe_id]) / len(recipe_ratings[recipe_id])

    return jsonify({
        "message": "Rating added",
        "average_rating": avg
    })


@ratings.route('/favorite/<int:recipe_id>', methods=['POST'])
def favorite_recipe(recipe_id):
    user = request.json.get("user", "default")

    if user not in favorites:
        favorites[user] = []

    favorites[user].append(recipe_id)

    return jsonify({"message": "Added to favorites"})


@ratings.route('/favorites/<user>', methods=['GET'])
def get_favorites(user):
    return jsonify(favorites.get(user, []))


@ratings.route('/rating/<int:recipe_id>', methods=['GET'])
def get_rating(recipe_id):
    if recipe_id not in recipe_ratings:
        return jsonify({"average_rating": 0})

    avg = sum(recipe_ratings[recipe_id]) / len(recipe_ratings[recipe_id])

    return jsonify({"average_rating": avg})
