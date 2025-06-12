"""Merge heads

Revision ID: 2f9197a089db
Revises: 3d1678038745, 426e329156c6
Create Date: 2025-06-12 10:53:25.541178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f9197a089db'
down_revision: Union[str, None] = ('3d1678038745', '426e329156c6')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
