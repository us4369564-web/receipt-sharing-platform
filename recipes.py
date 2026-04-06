from flask import Blueprint, request, jsonify

recipes = Blueprint('recipes', __name__)

recipe_list = []

@recipes.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    recipe = {
        "id": len(recipe_list) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "ingredients": data.get("ingredients"),
        "steps": data.get("steps"),
        "category": data.get("category")
    }
    recipe_list.append(recipe)
    return jsonify({"message": "Recipe created", "recipe": recipe})

@recipes.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipe_list)

@recipes.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.json
    for recipe in recipe_list:
        if recipe["id"] == recipe_id:
            recipe["title"] = data.get("title", recipe["title"])
            recipe["description"] = data.get("description", recipe["description"])
            return jsonify({"message": "Recipe updated"})
    return jsonify({"message": "Recipe not found"})

@recipes.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    for recipe in recipe_list:
        if recipe["id"] == recipe_id:
            recipe_list.remove(recipe)
            return jsonify({"message": "Recipe deleted"})
    return jsonify({"message": "Recipe not found"})
