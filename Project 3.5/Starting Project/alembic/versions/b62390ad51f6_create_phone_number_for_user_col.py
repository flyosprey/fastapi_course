"""create phone number for user col

Revision ID: b62390ad51f6
Revises: 
Create Date: 2023-08-01 11:38:27.690655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b62390ad51f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("phone_number", sa.Integer(), nullable=True))


def downgrade():
    op.drop_column("users", "phone_number")
