from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from backend.app.schemas.category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=500, description="Название товара")
    description: Optional[str] = Field(None, min_length=5, max_length=1000, description="Описание товара")
    price: float = Field(..., gt=0, description="Цена товара")
    image_url: Optional[str] = Field(None, min_length=10, max_length=255, description="Ссылка на изображение")
    category_id: int = Field(..., description="ID категории, к которой принадлежит товар")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="Уникальный ID продукта")
    category: CategoryResponse = Field(..., description="Категория продукта - подробнее")
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Общее количество товаров")