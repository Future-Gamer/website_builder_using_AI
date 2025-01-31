from sqlalchemy import CheckConstraint, UniqueConstraint, create_engine, Column, Integer, String, Sequence, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's users.db file
engine = create_engine('sqlite:///users.db')

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the User class which will be mapped to the users table
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(75), nullable=False, unique=True)
    email = Column(String(75), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    # __table_args__ = (
    #     UniqueConstraint('username', name='uq_user_username'),
    #     UniqueConstraint('email', name='uq_user_email'),
    #     CheckConstraint('LENGTH(password) >= 8', name='check_user_password_length')
    # )
    def __repr__(self):
        return f"<User(user_id='{self.user_id}', username='{self.username}', email='{self.email}', 'password='{self.password},' created_at='{self.created_at}')>"
    
# Create the users table in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create new users
new_user = User(username='Arpan Parekh', email='lucifer2003@gmail.com', password='password123')

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