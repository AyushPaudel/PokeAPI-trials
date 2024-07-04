"""Adding pokemon model

Revision ID: 45957e4adca1
Revises: 345ca0454e38
Create Date: 2024-07-04 15:08:51.846328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45957e4adca1'
down_revision: Union[str, None] = '345ca0454e38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemons',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('ability', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('type', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemons')
    # ### end Alembic commands ###
