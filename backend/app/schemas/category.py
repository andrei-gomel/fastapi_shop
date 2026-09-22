from typing import TYPE_CHECKING
from pydantic import BaseModel, Field, ConfigDict
# from .product import ProductBase

if TYPE_CHECKING:
    from .product import ProductBase

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, 
                      description="Category name")
    slug: str = Field(..., min_length=5, max_length=100, 
                      description="URL-friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category ID")    
    # В Pydantic v2 используется новый словарь ConfigDict вместо класса Config
    model_config = ConfigDict(from_attributes=True)
    
class CategoryProductResponse(CategoryResponse):
    products: list["ProductBase"] = Field(default=[], description="Список продуктов в категории")
    # total: int
    model_config = ConfigDict(from_attributes=True)
    
from . import product
CategoryProductResponse.model_rebuild(_types_namespace={"ProductBase": product.ProductBase})
