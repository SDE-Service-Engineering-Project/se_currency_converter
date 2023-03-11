import bcrypt
from spyne import TTableModel, UnsignedInteger32, Unicode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Generate a ComplexModelBase subclass with
# metadata information
TableModel = TTableModel()

# Initialize SQLAlchemy Environment
db = create_engine('sqlite:///:memory:')
TableModel.Attributes.sqla_metadata.bind = db


# Session Singleton
class Session:
    __instance = None

    @staticmethod
    def get_instance():
        if Session.__instance is None:
            Session()
        return Session.__instance

    def __init__(self):
        if Session.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Session.__instance = sessionmaker(bind=db)()


# Define user table
class User(TableModel):
    __tablename__ = 'user'
    __namespace__ = "ccs"
    __type_name__ = "credentials"

    id = UnsignedInteger32(pk=True)
    username = Unicode(32, min_len=4, pattern='[a-z0-9.]+', unique=True)
    password = Unicode(64, min_len=8)
    salt = Unicode(64)


# Create tables
TableModel.Attributes.sqla_metadata.create_all(
    checkfirst=True)


def initialize_user():
    # Initialize a user
    salt = bcrypt.gensalt()
    session = Session.get_instance()

    session.add(User(
        username="admin",
        password=bcrypt.hashpw(b"admin", salt),
        salt=salt
    ))
    session.commit()


initialize_user()
