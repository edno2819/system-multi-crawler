from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()

    def init_db(self):
        self.Base.metadata.create_all(bind=self.engine)
    
    def test_connection(self):
        try:
            # Execute a simple query to check the connection
            self.engine.execute("SELECT 1")
            print("Database connection established successfully.")
        except OperationalError:
            print("Failed to establish database connection.")

    def commit(self):
        try:
            self.db_session.commit()
        except:
            self.db_session.rollback()
            raise

    def close(self):
        self.db_session.close()



