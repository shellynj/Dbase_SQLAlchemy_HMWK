from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, CheckConstraint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

engine = create_engine('sqlite:///C:\\Users\\User\\PycharmProjects\\Dbase_SQLAlchemy_HMWK\\sql_alch.db')

engine.connect()

print(engine)

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')

    def __repr__(self):
        return "<Customer:{0}-{1}>".format(self.id, self.username)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(SmallInteger(), nullable=False)

    #     orders = relationship("Order", backref='customer')

    def __repr__(self):
        return "<Item:{0}-{1}>".format(self.id, self.name)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='quantity_check'),
    )


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, nullable=False)
    date_shipped = Column(DateTime())

    #     items = relationship("OrderLine")

    def __repr__(self):
        return "<Order:{0}>".format(self.id)


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")

    def __repr__(self):
        return "<OrderLine:{0}>".format(self.id)


Base.metadata.create_all(engine)


# Creating Session
#from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Inserting Data
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )



c3 = Customer(first_name="John",
              last_name="Lara",
              username="johnlara",
              email="johnlara@mail.com",
              address="3073 Derek Drive",
              town="Norfolk"
              )

c4 = Customer(first_name="Sarah",
              last_name="Tomlin",
              username="sarahtomlin",
              email="sarahtomlin@mail.com",
              address="3572 Poplar Avenue",
              town="Norfolk"
              )

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )



#----Add products
i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)





#---Create orders
o1 = Order(customer = c1)
o2 = Order(customer = c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item4 = OrderLine(order=o2, item=i2, quantity=4)


o3 = Order(customer = c1)

orderline1 = OrderLine(item = i1, quantity = 5)
orderline2 = OrderLine(item = i2, quantity = 10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

#--Querying Database

# all() method
session.query(Customer).all()
print("session.query(Customer).all()=", session.query(Customer).all())
#--------------------------
print("session.query(Item).all() session.query(Order).all()=", session.query(Item).all(), session.query(Order).all())

print(session.query(Customer))


q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

print("session.query(Customer.id, Customer.first_name).all()=", session.query(Customer.id, Customer.first_name).all())
session.query(Customer).count() # get the total number of records in the customers table
session.query(Item).count()  # get the total number of records in the items table
session.query(Order).count()  # get the total number of records in the orders table

# count() method
print("session.query(Customer).count()", session.query(Customer).count() ) # get the total number of records in the customers table
print("session.query(Item).count()", session.query(Item).count())  # get the total number of records in the items table
print("session.query(Order).count()", session.query(Order).count())  # get the total number of records in the orders table

# first() method
print("session.query(Customer).first()",session.query(Customer).first())
print("session.query(Item).first()", session.query(Item).first())
print("session.query(Order).first()", session.query(Order).first())

# get() method
print("session.query(Customer).get(1)",session.query(Customer).get(1))
print("session.query(Item).get(1)", session.query(Item).get(1))
print("session.query(Order).get(100)" , session.query(Order).get(100))

#filter() method
print("session.query(Customer).filter(Customer.first_name == 'John').all()",session.query(Customer).filter(Customer.first_name == 'John').all())

print(session.query(Customer).filter(Customer.first_name == 'John'))

print("session.query(Customer).filter(Customer.id <= 7, Customer.town == 'Norfolk').all()", session.query(Customer).filter(Customer.id <= 7, Customer.town == 'Norfolk').all())


print(session.query(Customer).filter(Customer.id <= 7, Customer.town.like("Nor%")))

print("-----------")
from sqlalchemy import or_, and_, not_

# find all customers who either live in Peterbrugh or Norfolk

print(session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all())




# find all customers whose first name is John and live in Norfolk

print(session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all())


# find all johns who don't live in Peterbrugh

print(session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all())
# IS NULL

print("session.query(Order).filter(Order.date_shipped == None).all()", session.query(Order).filter(Order.date_shipped == None).all())

#IS NOT NULL
print("session.query(Order).filter(Order.date_shipped != None).all()", session.query(Order).filter(Order.date_shipped != None).all())

# IN
print("session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()", session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all())

# NOT IN
print("session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()", session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all())

# BETWEEN
print("session.query(Item).filter(Item.cost_price.between(10, 50)).all()", session.query(Item).filter(Item.cost_price.between(10, 50)).all())

# NOT BETWEEN
print("session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()", session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all())

# LIKE
print("session.query(Item).filter(Item.name.like('%r')).all()", session.query(Item).filter(Item.name.like("%r")).all())
print("session.query(Item).filter(Item.name.ilike('w%')).all()", session.query(Item).filter(Item.name.ilike("w%")).all())

# NOT LIKE
print("session.query(Item).filter(not_(Item.name.like('W%'))).all()", session.query(Item).filter(not_(Item.name.like('W%'))).all())

# limit() method
print("session.query(Customer).limit(2).all()", session.query(Customer).limit(2).all())
print("session.query(Customer).filter(Customer.address.ilike('%avenue')).limit(2).all()", session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all())

print(session.query(Customer).limit(2))
print(session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2))

# offset() method
print("session.query(Customer).limit(2).offset(2).all()",session.query(Customer).limit(2).offset(2).all())

print(session.query(Customer).limit(2).offset(2))

# order_by() method

print("session.query(Item).filter(Item.name.ilike('wa%')).all()", session.query(Item).filter(Item.name.ilike("wa%")).all())
print("session.query(Item).filter(Item.name.ilike('wa%')).order_by(Item.cost_price).all()",session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all())

from sqlalchemy import desc
print(session.query(Item).filter(Item.name.ilike("wa%")).order_by(desc(Item.cost_price)).all())

# join() method
session.query(Customer).join(Order).all()

print(session.query(Customer).join(Order))

print(session.query(Customer.id, Customer.username, Order.id).join(Order).all())

# outerjoin() method
session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()

# group_by() method
from sqlalchemy import func
session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar()



# having() method
# find the number of customers lives in each town
session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()

#Dealing with Duplicates
from sqlalchemy import distinct
print(session.query(Customer.town).filter(Customer.id  < 10).all())
print(session.query(Customer.town).filter(Customer.id  < 10).distinct().all())

print(session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all())

#Casting




# Unions
s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
print(s1.union(s2).all())


# Union All
print(s1.union_all(s2).all())

# Updating Data
i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()

# update quantity of all quantity of items to 60 whose name starts with 'W'

print(session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch'))
session.commit()



