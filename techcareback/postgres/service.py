from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import  Session
from techcareback.postgres.models import SupplierModel, FamilyProductModel, InjectModels

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

injectModels = InjectModels()
supplierModel = SupplierModel()
familyProductModel = FamilyProductModel()

class PostgresService:
    def __init__(self):
        self.session = self.get_session()

    def get_session(self):
        session = Session(engine)
        return session

    SessionDep = Annotated[Session, Depends(get_session)]

    async def add_in_database(self, model: object) -> bool:
        session = self.get_session()
        session.add(model)
        session.commit()
        session.refresh(model)
        return True
    
    async def get_in_database(self, model: object) -> list[object]:
        return self.get_session().query(model).all()
    
    async def create_db_and_tables(self):
        injectModels.metadata.create_all(engine)