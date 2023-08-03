"""create users

Revision ID: f3f72286f0c2
Revises: 9427557d6130
Create Date: 2023-08-01 12:39:11.132547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3f72286f0c2'
down_revision = '9427557d6130'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column("address_id", sa.Integer(), nullable=True),
        sa.Column("email", sa.String(), index=True, unique=True),
        sa.Column("username", sa.String(), index=True, unique=True),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("phone_number", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), default=True),
    )
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_table("users")
