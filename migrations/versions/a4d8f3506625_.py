"""empty message

Revision ID: a4d8f3506625
Revises: 
Create Date: 2022-01-02 21:27:14.556629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4d8f3506625'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_users',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('avatar_url', sa.Text(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('URL', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_users')
    # ### end Alembic commands ###