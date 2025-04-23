from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, text, Text
from fastapi import FastAPI
from datetime import date


app = FastAPI()

engine =  create_async_engine('sqlite+aiosqlite:///app/Orders.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase):
    pass

class ProductModel(Base):
    __tablename__ = 'Products'
    Id: Mapped[int] = mapped_column(primary_key=True)
    Name_Products: Mapped[str] = mapped_column(nullable=True)
    Description: Mapped[str]
    Price: Mapped[float] = mapped_column(nullable=True)
    qualyty: Mapped[float]

class StatusModel(Base):
    __tablename__ = 'Status_Delivery'
    id: Mapped[int] = mapped_column(primary_key=True)
    Name_StatusDelivery: Mapped[str] = mapped_column(nullable=True)

class OrderModel(Base):
    __tablename__ = 'Orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    MakeDate: Mapped[date] = mapped_column(nullable=True)
    StatusDelivery_id: Mapped[str] = mapped_column(ForeignKey('Status_Delivery.id'), nullable=True)



@app.post('/setup_database')
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {'ok':True}







#@app.get('/')
#def root():
#    return('Hello World')