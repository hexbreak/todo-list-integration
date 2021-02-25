"""empty message

Revision ID: 06f564e2f9eb
Revises: 762402052503
Create Date: 2021-02-22 23:25:46.538337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06f564e2f9eb'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('todo_list', sa.String(length=250), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'todo_list')
    # ### end Alembic commands ###