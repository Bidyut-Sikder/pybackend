"""create new published column

Revision ID: 5933037775b2
Revises: 8c0ad967990f
Create Date: 2024-12-22 11:27:48.062847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5933037775b2'
down_revision: Union[str, None] = 'ce9b3d15c5b9'
# down_revision: Union[str, None] = '8c0ad967990f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    pass
