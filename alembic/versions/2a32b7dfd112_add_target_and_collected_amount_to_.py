from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2a32b7dfd112'
down_revision = '725a20faa306'
branch_labels = None
depends_on = None

def upgrade():
    # Step 1: Add 'target_amount' column
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('target_amount', sa.Float(), nullable=True))

    # Step 2: Add 'collected_amount' column
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('collected_amount', sa.Float(), nullable=True))

    # Step 3: Drop 'organiser_id' column
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.drop_column('organiser_id')


def downgrade():
    # Step 1: Add 'organiser_id' column back
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('organiser_id', sa.Integer(), nullable=True))

    # Step 2: Drop 'collected_amount' column
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.drop_column('collected_amount')

    # Step 3: Drop 'target_amount' column
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.drop_column('target_amount')
