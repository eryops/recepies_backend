from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID
from datetime import datetime

class Recipe(BaseModel):
    model_config = {"from_attributes": True}

    id: UUID
    name: str
    name_en: Optional[str] = None
    description: Optional[str] = None
    description_en: Optional[str] = None
    ingredients: list[dict[str, Any]]
    instructions: list[str]
    instructions_en: Optional[list[str]] = None
    youtube_url: Optional[str] = None
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None
    created_at: datetime
    updated_at: datetime | None = None

class RecipeCreate(BaseModel):
    name: str
    name_en: Optional[str] = None
    description: Optional[str] = None
    description_en: Optional[str] = None
    ingredients: list[dict[str, Any]]
    instructions: list[str]
    instructions_en: Optional[list[str]] = None
    youtube_url: Optional[str] = None
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None

class RecipeUpdate(BaseModel):
    name: Optional[str] = None
    name_en: Optional[str] = None
    description: Optional[str] = None
    description_en: Optional[str] = None
    ingredients: Optional[list[dict[str, Any]]] = None
    instructions: Optional[list[str]] = None
    instructions_en: Optional[list[str]] = None
    youtube_url: Optional[str] = None
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None