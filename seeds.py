from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


print(" Seeding DB...")

engine = create_engine('sqlite:///data.db') # the path that create engine needs to know what to talk to

Session = sessionmaker(bind=engine)  # talks to the database through the engine
session = Session()  # we talk to the session allows us to speak python to the database

session.query(User).delete()

users = [
    User(username="BugsBunnyFanatic"),
    User(username="WackyDaffy91"),
    User(username="TaxmanianTornado22"),
    User(username="SylvesterSneakylCAt"),
    User(username="RoadRunnerSpeedster"),

]

session.bulk_save_objects(users)
session.commit()

print(" Done seeding!")