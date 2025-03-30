from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base, User  # Импортируем User


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(String, nullable=False)

    chief_user = relationship('User', foreign_keys=[chief])

    members = relationship('User', secondary='department_members', back_populates='departments')

    def __init__(self, title, chief, email):
        self.title = title
        self.chief = chief
        self.email = email


class DepartmentMembers(Base):
    __tablename__ = 'department_members'
    department_id = Column(Integer, ForeignKey('departments.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
