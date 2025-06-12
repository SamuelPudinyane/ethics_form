"""Merge heads

Revision ID: 426e329156c6
Revises: 0310497184ba, a87e20169099
Create Date: 2025-06-12 02:55:19.164585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '426e329156c6'
down_revision: Union[str, None] = ('0310497184ba', 'a87e20169099')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
