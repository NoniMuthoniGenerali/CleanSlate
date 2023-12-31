"""Added CleaningTask model

Revision ID: 88f59f1e7abc
Revises: 3133054b8da5
Create Date: 2023-12-12 13:16:01.829323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88f59f1e7abc'
down_revision: Union[str, None] = '3133054b8da5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('claening_tasks',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('task_description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('cleaner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cleaner_id'], ['cleaners.cleaner_id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claening_tasks')
    # ### end Alembic commands ###
