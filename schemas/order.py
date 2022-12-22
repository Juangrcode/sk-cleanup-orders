# Python
from uuid import UUID
from enum import Enum
from datetime import datetime
from typing import Optional, Generic, TypeVar

# Pydantic
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')


class StatusMode(Enum):
    received = "received"
    inProcess = "inProcess"
    finish = "finish"


class OrderSchema(BaseModel):
    id: UUID = Field(...)
    order_number: int = Field(
        ...,
        gt=0,
        le=999,
        example=1
    )
    user_id: str = Field(
        ...,
        example="6383daa25e6687g5f00a3457"
    )
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Jorge"
    )
    phone_number: str = Field(
        ...,
        min_length=9,
        max_length=12,
        example="3000000000"
    )

    description: str = Field(
        ...,
        min_length=10,
        max_length=200,
        example="This is a description about order."
    )
    delivery_date: datetime = Field(
        ...,
        example="2022-01-01T00:00:00"
    )
    status: Optional[str] = Field(
        default=StatusMode.received,
        example=StatusMode.received
    )
    created_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True


class RequestOrder(BaseModel):
    parameter: OrderSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
