import re
from techcareback.postgres.models import SupplierModel
from techcareback.postgres.service import PostgresService
from techcareback.library.supplier.bo.supplier import Supplier
from techcareback.util.strings import SUPPLIER_ADRESS_ERROR, SUPPLIER_COMPANY_ERROR, SUPPLIER_CONTACT_ERROR, SUPPLIER_SIRET_ERROR

postgres_service = PostgresService()

class SupplierService:

    async def add_supplier(self, supplier: Supplier) -> bool:
        is_valid = await self.check_supplier_params(supplier)
        if is_valid:
            model = await self.supplierToSupplierModel(supplier)
            return await postgres_service.add_in_database(model)
        return False
    
    async def check_supplier_params(self, supplier: Supplier) -> bool:
        siret_regex = r'^\d{14}$'
        if not supplier.company_name:
            raise Exception(SUPPLIER_COMPANY_ERROR)
        if not supplier.siret or not re.match(siret_regex, supplier.siret):
            raise Exception(SUPPLIER_SIRET_ERROR)
        if not supplier.adress:
            raise Exception(SUPPLIER_ADRESS_ERROR)
        if not supplier.contact:
            raise Exception(SUPPLIER_CONTACT_ERROR)
        return True
    
    async def supplierToSupplierModel(self,supplier: Supplier) -> SupplierModel:
        supplierModel = SupplierModel()
        supplierModel.company_name = supplier.company_name
        supplierModel.siret = supplier.siret
        supplierModel.adress = supplier.adress
        supplierModel.contact = supplier.contact
        return supplierModel

    async def get_suppliers(self) -> list[object]:
        return await postgres_service.get_in_database(SupplierModel)