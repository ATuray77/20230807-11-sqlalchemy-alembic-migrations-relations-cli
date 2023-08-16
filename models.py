from sqlalchemy.orm import declarative_base

Base = declarative_base() # Base is like a sensor. whatever we define, base is going to learn from it and instances inherits form it
# when invoked, returns a base class that our python classes will inherit from. By inheriting from this class, we are establishing a connection betwen SQLAlchemy and our python classes
class User(Base):   # we are saying here that our User inherits from base
    __tablename__ = 'user'