"""Add servings to recipe

Revision ID: e923c58e1eb6
Revises: 781f4e795fdf
Create Date: 2026-03-30 14:43:32.683620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e923c58e1eb6'
down_revision: Union[str, Sequence[str], None] = '781f4e795fdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "recipes",
        sa.Column("servings", sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("recipes", "servings")

