

"""create posts table

Revision ID: ce9b3d15c5b9
Revises: 
Create Date: 2024-12-22 10:26:13.501166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce9b3d15c5b9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.Integer(),nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass

