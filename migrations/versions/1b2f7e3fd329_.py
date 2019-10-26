"""empty message

Revision ID: 1b2f7e3fd329
Revises: b1b7420bc905
Create Date: 2019-10-05 14:04:56.353219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b2f7e3fd329'
down_revision = 'b1b7420bc905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment_likes', type_='foreignkey')
    op.create_foreign_key(None, 'comment_likes', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment_likes', type_='foreignkey')
    op.create_foreign_key(None, 'comment_likes', 'blogs', ['comment_id'], ['id'])
    # ### end Alembic commands ###
