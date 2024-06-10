"""create tags

Revision ID: 6b029411b8ee
Revises: 21ae6c934e09
Create Date: 2024-06-10 12:37:48.144028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b029411b8ee'
down_revision: Union[str, None] = '21ae6c934e09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
