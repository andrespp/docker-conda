from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Database():

    connection_string = None
    engine = None
    echo = None

    def __init__(self, connection_string="sqlite:///data.db",echo=False):

        # Define db attributes
        self.connection_string=connection_string
        self.engine = create_engine(connection_string, echo=echo)
        self.echo = echo

        # Create database
        Base.metadata.create_all(self.engine)

    def __repr__(self):
        return f'SQLAlchemy Database Object\n' \
               f'connection_string = {self.connection_string}\n' \
               f'echo = {self.echo}'

    def session(self):
        Session = sessionmaker()
        session = Session(bind=self.engine)
        return session
