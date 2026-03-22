from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
import uuid

from app.schemas.recipe import Recipe, RecipeCreate, RecipeUpdate

router = APIRouter(prefix="/api/recipes", tags=["recipes"])


recipes: list[Recipe] = [
    Recipe(
        id="1",
        name="Spaghetti Carbonara",
        ingredients=["spaghetti", "eggs", "pancetta", "parmesan cheese"],
        created_at="2024-06-01T12:00:00Z",
        updated_at="2024-06-01T12:00:00Z",
    ),
    Recipe(
        id="2",
        name="Chicken Curry",
        ingredients=["chicken", "curry powder", "coconut milk", "onions"],
        created_at="2024-06-01T12:00:00Z",
        updated_at="2024-06-01T12:00:00Z",
    ),
    Recipe(
        id="3",
        name="Vegetable Stir Fry",
        ingredients=["broccoli", "carrots", "bell peppers", "soy sauce"],
        created_at="2024-06-01T12:00:00Z",
        updated_at="2024-06-01T12:00:00Z",
    ),
]

@router.get("")
def get_recipes():
    return recipes

@router.get("/{id}")
def get_recipe(id: str):
    recipe = next((r for r in recipes if r.id == id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/", status_code=201)
def create_recipe(data: RecipeCreate):
    new_recipe = Recipe(
        id=str(uuid.uuid4()),
        name=data.name,
        ingredients=data.ingredients,
        created_at=datetime.now(timezone.utc).isoformat(),
        updated_at=None,
    )
    recipes.append(new_recipe)
    return new_recipe

@router.put("/{id}")
def update_recipe(id: str, data: RecipeUpdate):
    recipe = next((r for r in recipes if r.id == id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    if data.name is not None:
        recipe.name = data.name
    if data.ingredients is not None:
        recipe.ingredients = data.ingredients

    recipe.updated_at = datetime.now(timezone.utc).isoformat()
    return recipe

@router.delete("/{id}", status_code=204)
def delete_recipe(id: str):
    global recipes
    recipes = [r for r in recipes if r.id != id]
    return None