from sqlmodel import Field, SQLModel

class InjectModels(SQLModel, table=False):
    pass

class SupplierModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    company_name: str
    siret: str
    adress: str
    contact: str

class FamilyProductModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    family_name: str
    specifications: str

class ProductModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    customs_code: str
    is_kit: bool
    ref: str
    serial_number: str
    img: str
    description: str
    public_price: str
    buying_price: str
    vat: str
    price_date: int
    units: str
    comments: str
    specifications: str
    family_product_id: int = Field(foreign_key="familyproductmodel.id")


class SippliersProductsModel(SQLModel, table=True):
    supplier_id: int = Field(foreign_key="suppliermodel.id", primary_key=True)
    product_id: int = Field(foreign_key="productmodel.id", primary_key=True)


