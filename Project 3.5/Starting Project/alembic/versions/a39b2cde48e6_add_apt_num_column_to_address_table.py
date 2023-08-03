"""Add apt_num column to address table

Revision ID: a39b2cde48e6
Revises: bae51Truebbf9a02
Create Date: 2023-08-03 08:29:11.485144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a39b2cde48e6'
down_revision = 'bae51Truebbf9a02'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("address", sa.Column("apt_num", sa.String(), nullable=True))


def downgrade():
    op.drop_column("address", "apt_num")
