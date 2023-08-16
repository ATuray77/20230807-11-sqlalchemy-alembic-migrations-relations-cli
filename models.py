from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, desc, create_engine

Base = declarative_base() # Base is like a sensor. whatever we define, base is going to learn from it and instances inherits form it
# when invoked, returns a base class that our python classes will inherit from. By inheriting from this class, we are establishing a connection betwen SQLAlchemy and our python classes
class User(Base):   # we are saying here that our User inherits from base
    __tablename__ = 'users'  # this is how we name our tables

    id = Column(Integer, primary_key=True) # this line should be in every schema you create
    username = Column(String)

    # how do we change the above info into a database? we use Alembic: a tool that manages migration.
    #We can ask alembic to autogenerate a version for us: alembic revision --autogenerate -m "message"

# to get a human readable printout
def __rpr__(self):
    return f"\n<User "\
        + f"id={self.id},"\
        + f"username={self.username},"
        
