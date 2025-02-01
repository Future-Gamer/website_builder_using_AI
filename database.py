from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float, create_engine, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')

# Create a base class for declarative class definitions
Base = declarative_base()

# User Profiles Table
class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    profile_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, primary_key=True)
    phone = Column(String)
    address = Column(String)
    password = Column(String, primary_key=True)
    confirm_password = Column(String)

    

# Users Table
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, ForeignKey('user_profiles.user_id'))
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    profiles = relationship("UserProfile", back_populates="user")
    websites = relationship("Website", back_populates="user")
    ai_generated_contents = relationship("AIGeneratedContent", back_populates="user")
    customization_settings = relationship("CustomizationSetting", back_populates="user")
    
    user = relationship("UserProfile", back_populates="profiles")


# Templates Table
class Template(Base):
    __tablename__ = 'templates'
    
    template_id = Column(Integer, primary_key=True)
    template_name = Column(String, nullable=False)
    description = Column(Text)
    preview_image_url = Column(String)
    created_at = Column(DateTime, nullable=False)

    components = relationship("TemplateComponent", back_populates="template")

# Template Components Table
class TemplateComponent(Base):
    __tablename__ = 'template_components'
    
    component_id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('templates.template_id'), nullable=False)
    component_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    template = relationship("Template", back_populates="components")

# Websites Table
class Website(Base):
    __tablename__ = 'websites'
    
    website_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    website_name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="websites")
    pages = relationship("WebsitePage", back_populates="website")
    ai_generated_contents = relationship("AIGeneratedContent", back_populates="website")
    customization_settings = relationship("CustomizationSetting", back_populates="website")
    analytics = relationship("Analytics", back_populates="website")

# Website Pages Table
class WebsitePage(Base):
    __tablename__ = 'website_pages'
    
    page_id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey('websites.website_id'), nullable=False)
    page_name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    website = relationship("Website", back_populates="pages")
    components = relationship("PageComponent", back_populates="page")

# Page Components Table
class PageComponent(Base):
    __tablename__ = 'page_components'
    
    component_id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('website_pages.page_id'), nullable=False)
    component_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    page = relationship("WebsitePage", back_populates="components")

# AI Generated Content Table
class AIGeneratedContent(Base):
    __tablename__ = 'ai_generated_content'
    
    content_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    website_id = Column(Integer, ForeignKey('websites.website_id'), nullable=False)
    generated_text = Column(Text, nullable=False)
    generated_image_url = Column(String)
    generated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="ai_generated_contents")
    website = relationship("Website", back_populates="ai_generated_contents")

# Customization Settings Table
class CustomizationSetting(Base):
    __tablename__ = 'customization_settings'
    
    setting_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    website_id = Column(Integer, ForeignKey('websites.website_id'), nullable=False)
    setting_name = Column(String, nullable=False)
    setting_value = Column(String, nullable=False)

    user = relationship("User", back_populates="customization_settings")
    website = relationship("Website", back_populates="customization_settings")

# Analytics Table
class Analytics(Base):
    __tablename__ = 'analytics'
    
    analytics_id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey('websites.website_id'), nullable=False)
    page_views = Column(Integer, nullable=False)
    unique_visitors = Column(Integer, nullable=False)
    bounce_rate = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    website = relationship("Website", back_populates="analytics")

Base.metadata.create_all(engine)

# Create the users table in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create new users
# new_user = Users_Profile(first_name='Arpan', last_name='Parekh', phone=6352307232, address='B-21, Rutuvilla Duplex, Tarsali, Vadodara')

# Add new users to the session
# session.add(new_user)

# Commit the transaction
session.commit()

# Query the database for all users
users = session.query(User).all()
for user in users:
    print(user)

# Close the session
session.close()