"""add location to user

Revision ID: 152f3d295071
Revises: 00000000
Create Date: 2020-03-05 11:37:25.012000

"""

# revision identifiers, used by Alembic.
revision = '152f3d295071'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('location', sa.String(length=128)))
    pass


def downgrade():
    pass
