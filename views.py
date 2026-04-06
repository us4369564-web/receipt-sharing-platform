from flask import Blueprint, jsonify

views = Blueprint('views', __name__)

recipes = [
    {"id": 1, "title": "Pasta", "category": "Italian", "rating": 4},
    {"id": 2, "title": "Burger", "category": "Fast Food", "rating": 5},
    {"id": 3, "title": "Biryani", "category": "Indian", "rating": 3}
]

@views.route('/recipes', methods=['GET'])
def all_recipes():
    return jsonify(recipes)

@views.route('/recipes/category/<category>', methods=['GET'])
def by_category(category):
    filtered = [r for r in recipes if r["category"].lower() == category.lower()]
    return jsonify(filtered)

@views.route('/recipes/latest', methods=['GET'])
def latest():
    return jsonify(recipes[::-1])

@views.route('/recipes/popular', methods=['GET'])
def popular():
    sorted_recipes = sorted(recipes, key=lambda x: x["rating"], reverse=True)
    return jsonify(sorted_recipes)

@views.route('/recipe/<int:id>', methods=['GET'])
def single_recipe(id):
    for r in recipes:
        if r["id"] == id:
            return jsonify(r)
    return jsonify({"message": "Recipe not found"})
