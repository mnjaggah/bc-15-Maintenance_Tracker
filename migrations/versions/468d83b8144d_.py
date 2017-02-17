"""empty message

Revision ID: 468d83b8144d
Revises: 
Create Date: 2017-02-16 17:06:51.448486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '468d83b8144d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=120), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_name', sa.String(length=64), nullable=True),
    sa.Column('staff_id', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('department', sa.String(length=200), nullable=True),
    sa.Column('date_of_request', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('admin_comments', sa.String(length=200), nullable=True),
    sa.Column('assignee_name', sa.String(length=64), nullable=True),
    sa.Column('assignee_phone_number', sa.String(length=64), nullable=True),
    sa.Column('photo', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
