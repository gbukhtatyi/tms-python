from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dsn = "sqlite:///test.db"

engine = create_engine(dsn, echo=False)

session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)


class Seller(Base):
    __tablename__ = "sellers"
    # Data
    company = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)


class Product(Base):
    __tablename__ = "products"
    # Relations
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    # Data
    name = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)


class User(Base):
    __tablename__ = "users"
    # Data
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class Order(Base):
    __tablename__ = "orders"
    # Relations
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    # Data
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)


# Drop tables
Base.metadata.drop_all(engine)

# Create tables
Base.metadata.create_all(engine)

with session() as connection:
    # Seed tables
    # * Users
    connection.add(User(username="user1", password="<PASSWORD>", email="user1@mail.com"))
    connection.add(User(username="user2", password="<PASSWORD>", email="user2@mail.com"))
    connection.add(User(username="user3", password="<PASSWORD>", email="user3@mail.com"))
    connection.commit()

    # * Sellers
    connection.add(Seller(company="Company 1", phone="123456789"))
    connection.add(Seller(company="Company 2", phone="123456789"))
    connection.add(Seller(company="Company 3", phone="123456789"))
    connection.commit()

    # * Products
    connection.add(Product(seller_id=1, name="Product 1", price=111))
    connection.add(Product(seller_id=2, name="Product 2", price=222))
    connection.add(Product(seller_id=3, name="Product 3", price=333))
    connection.commit()

    # Query tables
    # * Get Users
    query = select(User)
    users = connection.execute(query)
    for user in users.scalars():
        print(user.username, user.email)

    # * Get Sellers
    query = select(Seller)
    sellers = connection.execute(query)
    for seller in sellers.scalars():
        print(seller.company, seller.phone)

    # * Get Products
    query = select(Product)
    products = connection.execute(query)
    for product in products.scalars():
        print(product.name, product.price)

    # Create order
    queryUser = select(User)
    user = connection.execute(queryUser).first()[0]
    queryProduct = select(Product)
    product = connection.execute(queryProduct).first()[0]

    # Add order
    connection.add(Order(
        user_id=user.id,
        product_id=product.id,
        price=product.price,
        amount=2
    ))
    connection.commit()

    # # Print results
    query = select(Order)
    orders = connection.execute(query).scalars()
    for order in orders:
        print(
            'Order ID: ', order.id,
            'Order user_id: ', order.user_id,
            'Order product_id: ', order.product_id,
            'Order price: ', order.price,
            'Order amount: ', order.amount
        )
