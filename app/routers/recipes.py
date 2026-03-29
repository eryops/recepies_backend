from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
import uuid

from app.schemas.recipe import Recipe, RecipeCreate, RecipeUpdate

router = APIRouter(prefix="/api/recipes", tags=["recipes"])


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