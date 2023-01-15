from fastapi import APIRouter, Depends, Response, status

from ..models import GetData, PutData
from ..services import DropboxService


router = APIRouter(
    prefix='/operations',
    tags=['operations'],
)

@router.get(
    '/get_data',
    response_model=GetData,
    status_code=200
)
def get_data(
    file_name: str,
    operation_service: DropboxService = Depends()
):
    content = operation_service.get(file_name)
    return content

@router.put(
    '/put_data',
    response_model=PutData,
    status_code=200
)
def put_data(
    file_name: str,
    content: str,
    operation_service: DropboxService = Depends()
):
    return operation_service.put(file_name, content)