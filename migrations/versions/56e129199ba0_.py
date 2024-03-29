"""empty message

Revision ID: 56e129199ba0
Revises: b1b7420bc905
Create Date: 2019-10-26 18:00:09.872205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e129199ba0'
down_revision = 'b1b7420bc905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_type_name', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('event_name', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('details', sa.String(length=500), nullable=True),
    sa.Column('event_type_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['event_type_id'], ['event_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint(None, 'comment_likes', type_='foreignkey')
    op.create_foreign_key(None, 'comment_likes', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment_likes', type_='foreignkey')
    op.create_foreign_key(None, 'comment_likes', 'blogs', ['comment_id'], ['id'])
    op.drop_table('events')
    op.drop_table('event_types')
    # ### end Alembic commands ###
