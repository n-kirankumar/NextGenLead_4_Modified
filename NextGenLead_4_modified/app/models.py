# models.py

from sqlalchemy import Column, String, Integer, Date, BOOLEAN, BIGINT, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

"""
SQLAlchemy models for the 'productenquiryforms_4' and 'customerdetails_4' tables.
"""

# Create base class for models
Base = declarative_base()

# Create engine to connect to PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)

# Create session for database interaction
Session = sessionmaker(bind=engine)
session = Session()

# Define the ProductEnquiryForms_4 model
class ProductEnquiryForms_4(Base):
    """
    Represents the 'productenquiryforms_4' table in the database.
    This table stores customer product inquiries.
    """
    __tablename__ = 'productenquiryforms_4'

    CustomerName = Column("customername", String)
    Gender = Column("gender", String)
    Age = Column("age", Integer)
    Occupation = Column("occupation", String)
    MobileNo = Column("mobileno", BIGINT, primary_key=True)
    Email = Column("email", String)
    VehicleModel = Column("vechiclemodel", String)
    State = Column("state", String)
    District = Column("district", String)
    City = Column("city", String)
    ExistingVehicle = Column("existingvehicle", String)
    DealerState = Column("dealerstate", String)
    DealerTown = Column("dealertown", String)
    Dealer = Column("dealer", String)
    BriefAboutEnquiry = Column("briefaboutenquiry", Text)
    ExpectedDateOfPurchase = Column("expecteddateofpurchase", Date)
    IntendedUsage = Column("intendedusage", String)
    SentToDealer = Column("senttodealer", BOOLEAN)
    DealerCode = Column("dealercode", String)
    LeadId = Column("leadid", String)
    Comments = Column("comments", Text)
    CreatedDate = Column("createddate", Date)
    IsPurchased = Column("ispurchased", BOOLEAN)

# Define the CustomerDetails_4 model
class CustomerDetails_4(Base):
    """
    Represents the 'customerdetails_4' table in the database.
    This table stores customer details related to inquiries.
    """
    __tablename__ = 'customerdetails_4'

    LeadId = Column("leadid", String)
    CustomerName = Column("customername", String)
    MobileNo = Column("mobileno", BIGINT, primary_key=True)
    City = Column("city", String)
    Dealer = Column("dealer", String)
    DealerCode = Column("dealercode", String)
    SentToDealer = Column("senttodealer", BOOLEAN)

# Create the tables in PostgreSQL
Base.metadata.create_all(engine)
