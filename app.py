from flask import Flask, jsonify

app = Flask(__name__)

recipes = [
    {"id": 1, "name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "pancetta", "parmesan cheese"]},
    {"id": 2, "name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk", "onions"]},
    {"id": 3, "name": "Vegetable Stir Fry", "ingredients": ["broccoli", "carrots", "bell peppers", "soy sauce"]},
]

@app.route("/api/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)


if __name__ == "__main__":
    app.run(debug=True)
