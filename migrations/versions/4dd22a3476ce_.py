"""empty message

Revision ID: 4dd22a3476ce
Revises: ed826672816f
Create Date: 2018-10-28 15:04:59.963964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dd22a3476ce'
down_revision = 'ed826672816f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('price', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'price')
    # ### end Alembic commands ###
