from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from users import User, Base  # Replace 'your_database_module' with the actual name of your module

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
new_user = User(
    user_id=1,
    username='ArpanParekh',
    email='lucifer@gmail.com',
    password='password123',
    created_at=datetime.now()
)

# Add the new user to the session
session.add(new_user)

# Commit the transaction
session.commit()

# Query the database for all users
users = session.query(User).all()
for user in users:
    print(user)

# Close the session
session.close()
