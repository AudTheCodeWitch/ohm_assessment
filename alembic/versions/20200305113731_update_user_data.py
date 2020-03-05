"""update user data

Revision ID: 1b73fde8d2f1
Revises: 152f3d295071
Create Date: 2020-03-05 11:37:31.441000

"""

# revision identifiers, used by Alembic.
revision = '1b73fde8d2f1'
down_revision = '152f3d295071'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute(
        "UPDATE User SET point_balance = 5000 WHERE user_id = 1")

    op.execute(
        "UPDATE User SET location = 'USA' WHERE user_id = 2")

    op.execute(
        "UPDATE User SET tier = 'Silver' WHERE user_id = 3")
    pass


def downgrade():
    pass
