import re
from techcareback.library.familyproduct.bo.familyproduct import FamilyProduct
from techcareback.library.product.bo.product import Product
from techcareback.postgres.models import ProductModel, SuppliersProductsModel
from techcareback.postgres.service import PostgresService
from techcareback.util.strings import *

postgres_service = PostgresService()

class ProductService:

    async def add_product(self, product: Product) -> bool:
        is_valid = await self.check_product_params(product)
        if is_valid:
            model = await self.productToProductModel(product)
            product_added = await postgres_service.add_in_database(model)
            
            if product_added:
                suppliers_added = await self.add_product_suppliers(model.id, product.suppliers)
                return suppliers_added
            
        return False

    async def get_products(self) -> (list[object], list[object]):
        products = await postgres_service.get_in_database(ProductModel)
        all_suppliers = await postgres_service.get_in_database(SuppliersProductsModel)
        
        suppliers_by_product = []
        for product in products:
            product_suppliers = []
            for supplier_relation in all_suppliers:
                if supplier_relation.product_id == product.id:
                    product_suppliers.append(supplier_relation.supplier_id)
            suppliers_by_product.append(product_suppliers)
        
        return products, suppliers_by_product
    
    async def check_product_params(self, product: Product) -> bool:
        if not product.name or not isinstance(product.name, str):
            raise Exception(PRODUCT_NAME_ERROR)
        
        if not product.customs_code or not isinstance(product.customs_code, str):
            raise Exception(PRODUCT_CUSTOMS_CODE_ERROR)
        
        if not isinstance(product.is_kit, bool):
            raise Exception(PRODUCT_IS_KIT_ERROR)
        
        if not product.ref or not isinstance(product.ref, str):
            raise Exception(PRODUCT_REF_ERROR)
        
        if not product.serial_number or not isinstance(product.serial_number, str):
            raise Exception(PRODUCT_SERIAL_NUMBER_ERROR)
        
        if not product.img or not isinstance(product.img, str):
            raise Exception(PRODUCT_IMG_ERROR)
        
        if not product.description or not isinstance(product.description, str):
            raise Exception(PRODUCT_DESCRIPTION_ERROR)
        
        if not product.public_price or not isinstance(product.public_price, int):
            raise Exception(PRODUCT_PUBLIC_PRICE_ERROR)
        
        if not product.buying_price or not isinstance(product.buying_price, int):
            raise Exception(PRODUCT_BUYING_PRICE_ERROR)
        
        if not product.vat or not isinstance(product.vat, str):
            raise Exception(PRODUCT_VAT_ERROR)
        
        if not isinstance(product.date_price, int) or product.date_price <= 0:
            raise Exception(PRODUCT_PRICE_DATE_ERROR)
        
        if not product.units or not isinstance(product.units, int):
            raise Exception(PRODUCT_UNITS_ERROR)
        
        if not isinstance(product.comments, str):
            raise Exception(PRODUCT_COMMENTS_ERROR)
        
        if not isinstance(product.specifications, str):
            raise Exception(PRODUCT_SPECIFICATIONS_ERROR)
        
        if not isinstance(product.family_product_id, int) or product.family_product_id <= 0:
            raise Exception(PRODUCT_FAMILY_ID_ERROR)
        
        if not isinstance(product.suppliers, list):
            raise Exception(PRODUCT_SUPPLIERS_TYPE_ERROR)
        
        if not all(isinstance(supplier_id, int) and supplier_id > 0 for supplier_id in product.suppliers):
            raise Exception(PRODUCT_SUPPLIERS_ID_ERROR)
        
        if len(product.suppliers) == 0:
            raise Exception(PRODUCT_SUPPLIERS_EMPTY_ERROR)

        return True
    
    async def productToProductModel(self, product: Product) -> ProductModel:
        productModel = ProductModel(
            name=product.name,
            customs_code=product.customs_code,
            is_kit=product.is_kit,
            ref=product.ref,
            serial_number=product.serial_number,
            img=product.img,
            description=product.description,
            public_price=product.public_price,
            buying_price=product.buying_price,
            vat=product.vat,
            price_date=product.date_price,
            units=product.units,
            comments=product.comments,
            specifications=product.specifications,
            family_product_id=product.family_product_id
        )
        return productModel
    
    async def add_product_suppliers(self, product_id: int, supplier_ids: list[int]) -> bool:
        try:
            supplier_relations = [
                SuppliersProductsModel(
                    supplier_id=supplier_id,
                    product_id=product_id
                )
                for supplier_id in supplier_ids
            ]
            
            for relation in supplier_relations:
                success = await postgres_service.add_in_database(relation)
                if not success:
                    return False
            
            return True
            
        except Exception as e:
            print(f"{PRODUCT_SUPPLIERS_RELATION_ERROR}: {str(e)}")
            return False