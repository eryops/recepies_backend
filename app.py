from flask import Flask, jsonify, request

app = Flask(__name__)

recipes = [
    {"id": 1, "name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "pancetta", "parmesan cheese"]},
    {"id": 2, "name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk", "onions"]},
    {"id": 3, "name": "Vegetable Stir Fry", "ingredients": ["broccoli", "carrots", "bell peppers", "soy sauce"]},
]

@app.route("/api/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)

@app.route("/api/recipes/<int:id>", methods=["GET"])
def get_recipe(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipe)

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = {
        "id": len(recipes) + 1,
        **data
    }
    recipes.append(new_recipe)
    return jsonify(new_recipe), 201

@app.route('/api/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):      
    recipe = next((r for r in recipes if r["id"] == id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    data = request.json
    recipe["name"] = data.get("name", recipe["name"])
    recipe["ingredients"] = data.get("ingredients", recipe["ingredients"])
    return jsonify(recipe)

@app.route('/api/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    global recipes
    recipes = [r for r in recipes if r["id"] != id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
