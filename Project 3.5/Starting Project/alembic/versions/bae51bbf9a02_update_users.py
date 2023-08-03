"""Update users

Revision ID: bae51bbf9a02
Revises: f3f72286f0c2
Create Date: 2023-08-01 12:59:47.630764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bae51Truebbf9a02'
down_revision = 'f3f72286f0c2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("users", "fist_name")
    op.add_column("users", sa.Column("first_name", sa.String(), nullable=False))


def downgrade():
    pass
