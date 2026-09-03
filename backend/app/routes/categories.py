from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.category_service import CategoryService
from ..schemas.category import CategoryResponse

router = APIRouter(
    prefix="/api/categories",
    tags=['categories']
)

@router.get("", summary="Get all categories", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all_categories()

@router.get("/{category_id}", summary="Get category by ID", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category(category_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_id(category_id)

@router.get("/{category_slug}", summary="Get category by slug", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category_by_slug(category_slug: str, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_slug(category_slug)
