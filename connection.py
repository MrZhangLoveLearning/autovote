from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys,os
base_path=os.path.split(os.path.realpath(__file__))[0]
DB_CONNECT_STRING='sqlite:///'+base_path+'/testDB.db'
base_dir=base_path+'/'
if os.name=='nt':
	DB_CONNECT_STRING='sqlite:///'+base_path+'\\testDB.db'
	base_dir=base_path+'\\'
engine=create_engine(DB_CONNECT_STRING,echo=True)
from sqlalchemy.ext.declarative import declarative_base 
# base model
BaseModel=declarative_base()
# initialize datebase
def init_db():
    BaseModel.metadata.create_all(engine)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session

def drop_db():
    BaseModel.metadata.drop_all(engine)


# init_db()
# drop_db()