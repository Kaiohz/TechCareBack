from pydantic import BaseModel, Field


class Supplier(BaseModel): 
    company_name: str = Field(..., description="Name of the company")
    siret: str = Field(..., description="Siret of the company")
    adress: str = Field(..., description="Adress of the company")
    contact: str = Field(..., description="Contact of the company")

