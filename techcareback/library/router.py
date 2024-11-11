from fastapi import APIRouter, HTTPException

from techcareback.library.familyproduct.bo.familyproduct import FamilyProduct
from techcareback.library.product.bo.product import Product
from techcareback.library.supplier.bo.supplier import Supplier
from techcareback.library.supplier.service import SupplierService
from techcareback.library.familyproduct.service import FamilyProductService
from techcareback.library.product.service import ProductService
from techcareback.postgres.models import FamilyProductModel
from techcareback.util.logger import logger
from techcareback.util.strings import FAMILY_PRODUCT_ERROR, FAMILY_PRODUCT_SUCCESS, PRODUCT_ERROR, PRODUCT_SUCCESS, SUPPLIER_ERROR, SUPPLIER_SUCCESS

supplier_router = APIRouter()
supplier_service = SupplierService()
family_product_service = FamilyProductService()
product_service = ProductService()

@supplier_router.post("/supplier/add")
async def add_supplier(supplier: Supplier) -> dict:
    try:
        is_added = await supplier_service.add_supplier(supplier)
        if is_added:
            return {"message":f"{SUPPLIER_SUCCESS}"}
    except Exception as e:
        logger.error(f"{SUPPLIER_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=SUPPLIER_ERROR)
    
@supplier_router.post("/familyproduct/add")
async def add_supplier(familyproduct: FamilyProduct) -> dict:
    try:
        is_added = await family_product_service.add_family_product(familyproduct)
        if is_added:
            return {"message":f"{FAMILY_PRODUCT_SUCCESS}"}
    except Exception as e:
        logger.error(f"{FAMILY_PRODUCT_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=FAMILY_PRODUCT_ERROR)
    
@supplier_router.get("/familyproducts/get")
async def get_family_products() -> list:
    try:
        family_products = await family_product_service.get_family_product()
        return family_products
    except Exception as e:
        logger.error(f"{FAMILY_PRODUCT_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=FAMILY_PRODUCT_ERROR)
    
@supplier_router.post("/product/add")
async def add_product(product: Product) -> dict:
    try:
        is_added = await product_service.add_product(product)
        if is_added:
            return {"message":f"{PRODUCT_SUCCESS}"}
    except Exception as e:
        logger.error(f"{PRODUCT_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=PRODUCT_ERROR)

@supplier_router.get("/products/get")
async def get_products() -> dict:
    try:
        products, suppliers_by_product = await product_service.get_products()
        return {"products":products, "suppliers":suppliers_by_product}
    except Exception as e:
        logger.error(f"{PRODUCT_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=PRODUCT_ERROR)

@supplier_router.get("/suppliers/get")
async def get_suppliers() -> list:
    try:
        suppliers = await supplier_service.get_suppliers()
        return suppliers
    except Exception as e:
        logger.error(f"{SUPPLIER_ERROR} : {str(e)}")
        raise HTTPException(status_code=500, detail=SUPPLIER_ERROR)
