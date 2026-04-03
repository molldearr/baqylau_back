from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.farm.farm_schemas import FarmCreate, FarmRead
from api.receipts.receipt_schemas import ReceiptCreate
from business_logic.receipts.receipt_service import ReceiptService
from data_access.receipt.receipt_repository import ReceiptRepository
from data_access.db.session import get_db

router = APIRouter()


def get_receipt_service(db: AsyncSession = Depends(get_db)) -> ReceiptService:
    repo = ReceiptRepository(db)
    return ReceiptService(repo)


@router.get("/all", response_model=list[FarmRead])
async def get_all_receipts(
    service: ReceiptService = Depends(get_receipt_service),
):
    return await service.get_all_dishes()


@router.post("/:id", response_model=FarmRead)
async def create_farm(
    farm: ReceiptCreate,
    service: ReceiptService = Depends(get_receipt_service),
):
    try:
        return await service.create(farm)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
