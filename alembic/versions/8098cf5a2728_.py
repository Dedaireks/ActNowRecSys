""" 

Revision ID: 8098cf5a2728
Revises: 1a6f500bea0f
Create Date: 2024-04-15 12:35:29.984650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8098cf5a2728'
down_revision: Union[str, None] = '1a6f500bea0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stories', 'content',
               existing_type=sa.VARCHAR(length=2550),
               nullable=True)
    op.create_index(op.f('ix_stories_content'), 'stories', ['content'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stories_content'), table_name='stories')
    op.alter_column('stories', 'content',
               existing_type=sa.VARCHAR(length=2550),
               nullable=False)
    # ### end Alembic commands ###