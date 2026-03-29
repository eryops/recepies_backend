from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.recipe import Recipe, RecipeCreate, RecipeUpdate
from app.models.recipe import RecipeModel
from app.database import get_db

router = APIRouter(prefix="/api/recipes", tags=["recipes"])


@router.get("", response_model=list[Recipe])
def get_recipes(db: Session = Depends(get_db)):
    return db.query(RecipeModel).all()


@router.get("/{id}", response_model=Recipe)
def get_recipe(id: UUID, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == id).first()
    if not recipe:
        raise HTTPException(404, "Recipe not found")
    return recipe


@router.post("/", response_model=Recipe, status_code=201)
def create_recipe(data: RecipeCreate, db: Session = Depends(get_db)):
    recipe = RecipeModel(**data.model_dump())
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


@router.put("/{id}", response_model=Recipe)
def update_recipe(id: UUID, data: RecipeUpdate, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == id).first()
    if not recipe:
        raise HTTPException(404, "Recipe not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(recipe, key, value)

    db.commit()
    db.refresh(recipe)
    return recipe


@router.delete("/{id}", status_code=204)
def delete_recipe(id: UUID, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == id).first()
    if not recipe:
        raise HTTPException(404, "Recipe not found")

    db.delete(recipe)
    db.commit()
    return None