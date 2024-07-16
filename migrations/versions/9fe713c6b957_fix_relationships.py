"""Fix relationships

Revision ID: 9fe713c6b957
Revises: 
Create Date: 2024-07-12 22:19:50.436817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fe713c6b957'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('illness',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('body_part', sa.String(length=80), nullable=True),
    sa.Column('symptoms', sa.String(length=200), nullable=True),
    sa.Column('treatment', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('herbs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('health_benefits', sa.String(length=200), nullable=True),
    sa.Column('side_effects', sa.String(length=200), nullable=True),
    sa.Column('illness_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['illness_id'], ['illness.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_illness',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['illness_id'], ['illness.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'illness_id')
    )
    op.create_table('illness_herbs',
    sa.Column('illness_id', sa.Integer(), nullable=False),
    sa.Column('herbs_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['herbs_id'], ['herbs.id'], ),
    sa.ForeignKeyConstraint(['illness_id'], ['illness.id'], ),
    sa.PrimaryKeyConstraint('illness_id', 'herbs_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('illness_herbs')
    op.drop_table('user_illness')
    op.drop_table('herbs')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_name'))

    op.drop_table('user')
    op.drop_table('illness')
    # ### end Alembic commands ###
