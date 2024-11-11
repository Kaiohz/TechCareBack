import re
from techcareback.library.familyproduct.bo.familyproduct import FamilyProduct
from techcareback.postgres.models import FamilyProductModel
from techcareback.postgres.service import PostgresService
from techcareback.util.strings import FAMILY_PRODUCT_NAME_ERROR

postgres_service = PostgresService()

class FamilyProductService:

    async def add_family_product(self, familyproduct: FamilyProduct) -> bool:
        is_valid = await self.check_family_product_params(familyproduct)
        if is_valid:
            model = await self.familyProductToFamilyProductModel(familyproduct)
            return await postgres_service.add_in_database(model)
        return False
    
    async def get_family_product(self) -> list[object]:
        return await postgres_service.get_in_database(FamilyProductModel)
    
    async def check_family_product_params(self, familyproduct: FamilyProduct) -> bool:
        if not familyproduct.family_name:
            raise Exception(FAMILY_PRODUCT_NAME_ERROR)
        return True
    
    async def familyProductToFamilyProductModel(self,familyProduct: FamilyProduct) -> FamilyProductModel:
        familyProductModel = FamilyProductModel()
        familyProductModel.family_name = familyProduct.family_name
        familyProductModel.specifications = familyProduct.specifications
        return familyProductModel