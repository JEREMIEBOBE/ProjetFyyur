"""empty message

Revision ID: 917dd9f639d0
Revises: c3846bb1d782
Create Date: 2022-08-15 02:47:35.652207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917dd9f639d0'
down_revision = 'c3846bb1d782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('show_venue_id_fkey', 'show', type_='foreignkey')
    op.create_foreign_key(None, 'show', 'venue', ['venue_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.create_foreign_key('show_venue_id_fkey', 'show', 'venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###
