from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class Recipe(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    ingredients: list[str]
    instructions: list[str]
    youtube_url: Optional[str] = None
    prep_time_minutes: Optional[int] = None
    cook_time_minutes: Optional[int] = None
    created_at: datetime
    updated_at: datetime | None = None

class RecipeCreate(BaseModel):
    name: str
    description: str | None = None
    ingredients: list[str]
    instructions: list[str] | None = None
    youtube_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None

class RecipeUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    ingredients: list[str] | None = None
    instructions: list[str] | None = None
    youtube_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
