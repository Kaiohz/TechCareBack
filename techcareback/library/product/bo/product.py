from pydantic import BaseModel

class Product(BaseModel):
    id: int
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
    family_product_id: int