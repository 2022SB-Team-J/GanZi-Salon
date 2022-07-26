"""create user table

Revision ID: 6c97e70bd8cd
Revises: 
Create Date: 2022-07-26 15:35:38.203718

"""

# >>https://blog.neonkid.xyz/257
# 참고링크 >  https://blog.outsider.ne.kr/1143
#        >https://github.com/zusdn90/fastapi-signUp-API/blob/main/backend/migrations/local/versions/df2c8de0cdaa_db_migration.py
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c97e70bd8cd'
down_revision = None
branch_labels = None
depends_on = None

# 마이그래이션 버전을 적용할 때 실행
def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_idx', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.String(length=20), nullable=False, comment='아이디'),
        sa.Column('username', sa.String(length=20), nullable=False, comment='이름'),
        sa.Column('password', sa.String(length=20), nullable=False, comment='비밀번호'),
        sa.Column('gender', sa.String(length=2), nullable=False, comment='성별'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True, comment='생성일'),
        sa.Column('upload_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True, comment='수정일'),
        sa.Column('is_active', sa.Boolean, nullable=False, comment='활동 여부'),

        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('user_id'),
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)


# 적용한 마이그래이션을 취소할 때 실행
def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_auth_id'), table_name='users')
    op.drop_table('users')