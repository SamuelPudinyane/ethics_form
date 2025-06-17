"""Merge heads

Revision ID: c4aed6e80625
Revises: 835ab99b5f51, b2c90d453c8a
Create Date: 2025-06-17 11:45:52.745645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4aed6e80625'
down_revision: Union[str, None] = ('835ab99b5f51', 'b2c90d453c8a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
