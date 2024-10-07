from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, BigInteger
from sqlalchemy.orm import relationship

from app.database import Base, engine


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String)
    phone = Column(String(20), nullable=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    region = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    school = Column(String(100), nullable=True)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    joined_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, username={self.username})"


class TestSingle(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)
    created_at = Column(DateTime)
    started_at = Column(DateTime, nullable=True)
    ended_at = Column(DateTime, nullable=True)
    is_ongoing = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    answers = Column(String(100), nullable=True)
    owner = relationship("User")


class ParticipationSingle(Base):
    __tablename__ = 'participation'
    participationID = Column(Integer, primary_key=True)
    userID = Column(BigInteger, ForeignKey('user.id'))
    testID = Column(Integer, ForeignKey('test.id'))
    score = Column(Integer)
    submitted_at = Column(DateTime)
    user = relationship("User")
    test = relationship("Test")


# Additional models

class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


def init_models():
    print("DEBUG: init_models() is working!")
    Base.metadata.create_all(bind=engine)