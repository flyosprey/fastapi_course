"""add address table

Revision ID: db250536da73
Revises: b62390ad51f6
Create Date: 2023-08-01 11:53:04.698816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db250536da73'
down_revision = 'b62390ad51f6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("address1", sa.String(), nullable=False),
        sa.Column("address2", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("postalcode", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table("address")
