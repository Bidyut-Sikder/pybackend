"""create new coulmn

Revision ID: 8c0ad967990f
Revises: ce9b3d15c5b9
Create Date: 2024-12-22 11:12:24.347542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c0ad967990f'
down_revision: Union[str, None] = 'ce9b3d15c5b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
