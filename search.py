from flask import Blueprint, request, jsonify

search = Blueprint('search', __name__)

recipes = [
    {"id": 1, "title": "Pasta", "ingredients": "cheese,tomato", "category": "Italian"},
    {"id": 2, "title": "Biryani", "ingredients": "rice,chicken", "category": "Indian"},
    {"id": 3, "title": "Burger", "ingredients": "bread,cheese", "category": "Fast Food"}
]

@search.route('/search', methods=['GET'])
def search_recipes():
    query = request.args.get('q', '').lower()
    
    filtered = []
    for recipe in recipes:
        if (query in recipe["title"].lower() or
            query in recipe["ingredients"].lower() or
            query in recipe["category"].lower()):
            filtered.append(recipe)

    return jsonify(filtered)


@search.route('/filter/category/<category>', methods=['GET'])
def filter_category(category):
    filtered = [r for r in recipes if r["category"].lower() == category.lower()]
    return jsonify(filtered)
