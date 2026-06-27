from sqlalchemy  import Column,Integer,String,Enum,ForeignKey
from database import Base,engine,SessionLocal

Base = declarative_base()

class Job(base):
    __tablename__="jobs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    descripton = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey('companies.id'))