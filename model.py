from sqlalchemy import Column
from sqlalchemy.types import String
import connection
Base = connection.BaseModel


class Account(Base):
	__tablename__='account'
	account = Column(String(100), primary_key=True)
	passwd=Column(String(100))

# connection.init_db()