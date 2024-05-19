from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

engine = create_engine(URL)
Base = declarative_base()

class Employee(Base):
    """representing class name and metods"""

    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    date_of_birth = Column(Date)
    position = Column(String)
    salary = Column(Integer)
    start_date = Column(Date)


# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()


def add_employee(name, surname, date_of_birth, position, salary, start_date):
    name = input("Enter employee's name: ")
    surname = input("Enter employee's surname: ")
    date_of_birth = input("Enter employee's date of birth (YYYY-MM-DD): ")
    position = input("Enter employee's position: ")
    salary = int(input("Enter employee's salary: "))
    start_date = datetime.date.today()

