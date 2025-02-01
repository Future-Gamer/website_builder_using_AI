from xml.dom.expatbuilder import InternalSubsetExtractor
from colorama import Fore
from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint, create_engine, Column, Integer, String, Sequence, DateTime, false, func, null, true
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's users.db file
engine = create_engine('sqlite:///users.db')

# Create a base class for declarative class definitions
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(75), nullable=False, unique=True)
    email = Column(String(75), nullable=False, unique=True)
    password = Column(String(75), nullable=False)
    created_at = Column(DateTime, default=func.now())
    
class ai_Generated_Content(Base):
    __tablename__ = 'ai_generated_content'
    content_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    

# Define the User class which will be mapped to the users table
class Users_Profile(Base):
    __tablename__ = 'users_profile'
    profile_id = Column(Integer, Sequence('profile_id_seq'), primary_key=True)
    user_id = Column(Integer, Sequence('user_id_seq'), ForeignKey('users.user_id'))
    first_name = Column(String(75), nullable=False, unique=True)
    last_name = Column(String(75), nullable=False, unique=True)
    phone = Column(Integer, nullable=False, unique=True)
    address = Column(String(100), nullable=False, unique=True)
    
    # __table_args__ = (
    #     CheckConstraint('LENGTH(phone) >= 10', name='check_phone_number')
    # )
    def __repr__(self):
        return f"<Users_Profile(user_id='{self.profile_id}', username='{self.user_id}', email='{self.first_name}', 'password='{self.last_name},' created_at='{self.phone}', address='{self.address}')>"
    
# Create the users table in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create new users
new_user = Users_Profile(first_name='Arpan', last_name='Parekh', phone=6352307232, address='B-21, Rutuvilla Duplex, Tarsali, Vadodara')

# Add new users to the session
session.add(new_user)

# Commit the transaction
session.commit()

# Query the database for all users
users = session.query(User).all()
for user in users:
    print(user)

# Close the session
session.close()
