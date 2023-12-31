"""empty message

Revision ID: ec4947284bd4
Revises: 
Create Date: 2023-08-21 13:41:32.533742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4947284bd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###
