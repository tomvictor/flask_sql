"""create model

Revision ID: 20ed485018de
Revises: 
Create Date: 2022-04-28 17:35:20.058223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ed485018de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('identifier', sa.VARCHAR(length=36), nullable=False),
    sa.Column('doc', sa.JSON(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('address_line', sa.VARCHAR(length=128), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('state', sa.VARCHAR(length=64), nullable=False),
    sa.Column('country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('zip', sa.VARCHAR(length=64), nullable=False),
    sa.Column('phone', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_organization_identifier'), 'organization', ['identifier'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_organization_identifier'), table_name='organization')
    op.drop_table('organization')
    # ### end Alembic commands ###
