"""Add seller_id field to Product model

Revision ID: 1ca3817dcbbf
Revises: b8d68fd4f2b1
Create Date: 2025-03-22 00:52:25.978224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca3817dcbbf'
down_revision = 'b8d68fd4f2b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('stock',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('stock',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
