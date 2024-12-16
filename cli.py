import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,TM,Student


DATABASE_URL = "sqlite:///tms.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    # Initialize Database
    Base.metadata.create_all(engine)
    print("Database Initialized")

def create_tm():
    # create new tm
    name = input("Enter TM name: ")
    email = input("Enter TM email: ")
    tm = TM(name=name,email=email)
    session.add(tm)
    session.commit()
    print(f"TM '{name}' created with ID {tm.id}")

def update_tm():
    tm_id = int(input("Enter TM ID to update: "))
    tm = session.get(TM,tm_id)
    if not tm:
        print(f"TM with ID {tm_id} does not exist.")
        return
    tm.name = input(f"Enter new name for TM (current: {tm.name}): ") or tm.name
    tm.email = input(f"Enter new email for TM (current: {tm.email}): ") or tm.email
    session.commit()
    print(f"TM ID {tm_id} updated successfully")

def delete_tm()