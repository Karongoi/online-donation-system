"""Add organiser_id foreign key to causes

Revision ID: d13499fb11ae
Revises: 2a32b7dfd112
Create Date: 2025-05-29 08:14:04.243395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd13499fb11ae'
down_revision: Union[str, None] = '2a32b7dfd112'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('causes') as batch_op:
        batch_op.alter_column('organiser_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)
        batch_op.drop_column('total_amount')
        batch_op.drop_column('balance')
        batch_op.drop_column('deadline')


def downgrade() -> None:
    with op.batch_alter_table('causes') as batch_op:
        batch_op.add_column(sa.Column('deadline', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('balance', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('total_amount', sa.INTEGER(), nullable=True))
        batch_op.alter_column('organiser_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)
