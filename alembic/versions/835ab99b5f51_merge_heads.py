"""Merge heads

Revision ID: 835ab99b5f51
Revises: 2f9197a089db, 8b22733373dc
Create Date: 2025-06-16 13:50:25.643998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '835ab99b5f51'
down_revision: Union[str, None] = ('2f9197a089db', '8b22733373dc')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
