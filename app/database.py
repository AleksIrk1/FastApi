from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import ForeignKey, text, Text
from datetime import date
from sql_enum import StatusOrder

engine =  create_async_engine('sqlite+aiosqlite:///app/Orders.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    #pass

class Product(Base):
    name_products: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=False)
    quantitys_produ: Mapped[float]

class Order(Base):
    make_date: Mapped[date] = mapped_column(nullable=False)
    status_delivery_id: Mapped[StatusOrder] = mapped_column(default=StatusOrder.in_progress, server_default="'in_progress'")

class OrderItem(Base):
    orders_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    products_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity_orders_item: Mapped[int] = mapped_column(nullable=False)