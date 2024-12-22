"""adding name column

Revision ID: 1bf410e8358f
Revises: 5933037775b2
Create Date: 2024-12-22 11:36:00.573444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bf410e8358f'
down_revision: Union[str, None] = '5933037775b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('name',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','name')
    pass
