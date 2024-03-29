"""Changed column channels to JSON

Revision ID: 159ddccc1ed1
Revises: 606542323b0b
Create Date: 2024-03-07 15:41:01.985401

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '159ddccc1ed1'
down_revision = '606542323b0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jb_bot', sa.Column('channels', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jb_bot', 'channels')
    # ### end Alembic commands ###