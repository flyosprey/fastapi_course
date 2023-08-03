"""Create address_id to users

Revision ID: 9427557d6130
Revises: db250536da73
Create Date: 2023-08-01 12:06:07.286247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9427557d6130'
down_revision = 'db250536da73'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
