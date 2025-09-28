"""rename students.email -> email_address

Revision ID: d22d7a50e099
Revises: 791279dd0760
Create Date: 2025-09-28 17:03:28.319078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd22d7a50e099'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "students",
        "email",
        new_column_name="email_address",
    )


def downgrade() -> None:
    op.alter_column(
        "students",
        "email_address",
        new_column_name="email",
        existing_type=sa.String(length=55),
    )
