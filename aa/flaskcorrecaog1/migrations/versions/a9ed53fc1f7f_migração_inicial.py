"""Migração Inicial

Revision ID: a9ed53fc1f7f
Revises: 
Create Date: 2024-10-11 09:31:03.409670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9ed53fc1f7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id_planeta', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('distancia_sol', sa.Integer(), nullable=True),
    sa.Column('numero_satelites', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_planeta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planetas')
    # ### end Alembic commands ###
