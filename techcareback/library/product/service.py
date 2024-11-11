import re
from techcareback.library.familyproduct.bo.familyproduct import FamilyProduct
from techcareback.library.product.bo.product import Product
from techcareback.postgres.models import ProductModel
from techcareback.postgres.service import PostgresService

postgres_service = PostgresService()

class ProductService:

    async def add_product(self, product: Product) -> bool:
        is_valid = await self.check_product_params(product)
        if is_valid:
            model = await self.productToProductModel(product)
            return await postgres_service.add_in_database(model)
        return False
    
    async def check_product_params(self, product: Product) -> bool:
        if not product.name:
            raise Exception("")
        return True
    
    async def productToProductModel(self,product: Product) -> ProductModel:
        productModel = ProductModel()
        productModel.name = product.name

        return productModel