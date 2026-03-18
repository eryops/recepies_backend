from flask import Flask, jsonify, request
import uuid 
from datetime import datetime, timezone
from utils.case_conversion import camelize_dict
app = Flask(__name__)

recipes = [
    {"id": "1", "name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "pancetta", "parmesan cheese"], "created_at": "2024-06-01T12:00:00Z", "updated_at": "2024-06-01T12:00:00Z"},
    {"id": "2", "name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk", "onions"], "created_at": "2024-06-01T12:00:00Z", "updated_at": "2024-06-01T12:00:00Z"},
    {"id": "3", "name": "Vegetable Stir Fry", "ingredients": ["broccoli", "carrots", "bell peppers", "soy sauce"], "created_at": "2024-06-01T12:00:00Z", "updated_at": "2024-06-01T12:00:00Z"},
]

@app.route("/api/recipes", methods=["GET"])
def get_recipes():
    return jsonify([camelize_dict(recipe) for recipe in recipes])

@app.route("/api/recipes/<string:id>", methods=["GET"])
def get_recipe(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(camelize_dict(recipe))

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        **data
    }
    recipes.append(new_recipe)
    return jsonify(camelize_dict(new_recipe)), 201

@app.route('/api/recipes/<string:id>', methods=['PUT'])
def update_recipe(id):      
    recipe = next((r for r in recipes if r["id"] == id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    data = request.json
    for key, value in data.items():
        recipe[key] = value

    recipe["updated_at"] = datetime.now(timezone.utc).isoformat()
    return jsonify(camelize_dict(recipe))

@app.route('/api/recipes/<string:id>', methods=['DELETE'])
def delete_recipe(id):
    global recipes
    recipes = [r for r in recipes if r["id"] != id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
