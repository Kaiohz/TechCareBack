from pydantic import BaseModel, Field


class FamilyProduct(BaseModel): 
    family_name: str = Field(..., description="Name of family product")
    specifications: str = Field(..., description="Specifications for the family product")

