"""v1-contacts-remove-json

Revision ID: 2ab74e9499c0
Revises: 7c527dcfae03
Create Date: 2022-06-22 15:00:02.022190

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "2ab74e9499c0"
down_revision = "7c527dcfae03"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("contact", "invitation")
    op.drop_column("contact", "connection")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "contact",
        sa.Column(
            "connection",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "contact",
        sa.Column(
            "invitation",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
    )
    # ### end Alembic commands ###
