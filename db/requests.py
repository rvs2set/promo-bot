from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select
from db.models import Base, Partner, Promocode

DB_FILE = "bot.db"
engine = create_async_engine(f"sqlite+aiosqlite:///{DB_FILE}", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with async_session() as session:
        res = await session.execute(select(Partner))
        if not res.scalar_one_or_none():
            demo_partner = Partner(
                name="Яндекс Музыка",
                channel_id="@telegram",
                channel_url="https://t.me/telegram",
                is_active=True
            )
            session.add(demo_partner)
            await session.commit()
            
            session.add_all([
                Promocode(partner_id=1, code="FEST2026-1"),
                Promocode(partner_id=1, code="FEST2026-2")
            ])
            await session.commit()
    print("База данных успешно инициализирована через модуль db!")
