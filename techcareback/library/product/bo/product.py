from pydantic import BaseModel

class Product(BaseModel):
    name: str
    customs_code: str
    is_kit: bool
    ref: str
    serial_number: str
    img: str
    description: str
    public_price: int
    buying_price: int
    vat: str
    date_price: int
    units: int
    comments: str
    specifications: str
    family_product_id: int
    suppliers: list[int]