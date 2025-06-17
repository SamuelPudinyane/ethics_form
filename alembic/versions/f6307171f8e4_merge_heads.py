"""Merge heads

Revision ID: f6307171f8e4
Revises: 7a3cde0a05b6, c4aed6e80625
Create Date: 2025-06-17 14:20:59.774957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6307171f8e4'
down_revision: Union[str, None] = ('7a3cde0a05b6', 'c4aed6e80625')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
