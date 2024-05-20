

class Employees(Base):
    __tablename__ = 'Employee'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    last_name = Column("Pavardė", String)
    birthdate = Column("Gimimo data", DateTime)
    position = Column("Pareigos", String)
    salary = Column("Atlyginimas", Float)
    working_since = Column("Dirba nuo", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, last_name, birthdate, position, salary):
        self.name = name
        self.last_name = last_name
        self.birthdate = birthdate
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.id} {self.name} {self.last_name}, {self.position} {self.working_since}"