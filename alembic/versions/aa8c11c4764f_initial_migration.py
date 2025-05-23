"""initial_migration

Revision ID: aa8c11c4764f
Revises: 1f75b3c2a8d1
Create Date: 2025-05-21 18:04:33.003730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa8c11c4764f'
down_revision: Union[str, None] = '1f75b3c2a8d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form_c', sa.Column('vulnerable', sa.PickleType(), nullable=True))
    op.add_column('form_c', sa.Column('vulnerable_other', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('vulnerable_comments', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('activity', sa.PickleType(), nullable=True))
    op.add_column('form_c', sa.Column('activity_other', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('activity_comments', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('consideration', sa.PickleType(), nullable=True))
    op.add_column('form_c', sa.Column('consideration_comments', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('risk_level', sa.String(length=50), nullable=True))
    op.add_column('form_c', sa.Column('justify', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('risk_benefits', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('risk_mitigation', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('executive_summary', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('research_questions', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('research_purpose', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('secondary_data_info', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('exemption_reason', sa.Text(), nullable=True))
    op.add_column('form_c', sa.Column('eclaration_name', sa.String(length=255), nullable=True))
    op.add_column('form_c', sa.Column('full_name', sa.String(length=255), nullable=True))
    op.add_column('form_c', sa.Column('submission_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('form_c', 'submission_date')
    op.drop_column('form_c', 'full_name')
    op.drop_column('form_c', 'eclaration_name')
    op.drop_column('form_c', 'exemption_reason')
    op.drop_column('form_c', 'secondary_data_info')
    op.drop_column('form_c', 'research_purpose')
    op.drop_column('form_c', 'research_questions')
    op.drop_column('form_c', 'executive_summary')
    op.drop_column('form_c', 'risk_mitigation')
    op.drop_column('form_c', 'risk_benefits')
    op.drop_column('form_c', 'justify')
    op.drop_column('form_c', 'risk_level')
    op.drop_column('form_c', 'consideration_comments')
    op.drop_column('form_c', 'consideration')
    op.drop_column('form_c', 'activity_comments')
    op.drop_column('form_c', 'activity_other')
    op.drop_column('form_c', 'activity')
    op.drop_column('form_c', 'vulnerable_comments')
    op.drop_column('form_c', 'vulnerable_other')
    op.drop_column('form_c', 'vulnerable')
    # ### end Alembic commands ###
