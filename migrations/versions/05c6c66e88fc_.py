"""empty message

Revision ID: 05c6c66e88fc
Revises: 
Create Date: 2020-10-29 08:18:32.680456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c6c66e88fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('yanse', sa.String(length=256), nullable=False),
    sa.Column('m', sa.String(length=256), nullable=False),
    sa.Column('x', sa.String(length=256), nullable=False),
    sa.Column('xl', sa.String(length=256), nullable=False),
    sa.Column('xxl', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pro_sup',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'supplier_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pro_sup')
    op.drop_table('color')
    # ### end Alembic commands ###
