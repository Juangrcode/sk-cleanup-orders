# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Body, Path, Depends, status, HTTPException

# SqlAlchemy
from sqlalchemy.orm import Session

# Config DB
from config.db import get_db

# Models
from models.order import Order

# Schemas
from schemas.order import OrderSchema


# Create the Router api for FastAPI
order = APIRouter()


# Define de API endpoints

# Get all Orders
@order.get(
    path="/api/orders",
    response_model=List[OrderSchema],
    status_code=status.HTTP_200_OK,
    summary="Get all Orders",
    tags=["Orders"]
)
def get_orders(
    db: Session = Depends(get_db),
):
    """
    Get all Orders

    This path operation get all orders in the app.

    Returns a json with the all orders information:
      - id: UUID
      - order_number: int
      - user_id: str
      - name: str
      - phone_number: str
      - description: str
      - delivery_date: datetime
      - status: Optional[str]
      - created_at: Optional[datetime]
    """

    return db.query(Order).all()


# Get Order by ID
@order.get(
    path="/api/orders/{order_id}",
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK,
    summary="Get Order by ID",
    tags=["Orders"]
)
def get_order(
    db: Session = Depends(get_db),
    order_id: str = Path(
        ...,
        title="Order ID",
        description="This is a Order ID.",
        example="efa1439c-a967-4b97-a5c0-7b4e42fe87a3"
    )
):
    """
    Get Order by ID

    This path operation get one order by ID in the app.

    Parameters:
      - Request path parameter
        - order_id: UUID

    Returns a json with the all orders information:
      - id: UUID
      - order_number: int
      - user_id: str
      - name: str
      - phone_number: str
      - description: str
      - delivery_date: datetime
      - status: Optional[str]
      - created_at: Optional[datetime]
    """

    order = db.query(Order).filter(Order.id == order_id).first()

    if order:
        return order
    else:
        return HTTPException(status_code=404, detail="Order not found")


# Create Order
@order.post(
    path="/api/orders",
    response_model=OrderSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create Order",
    tags=["Orders"]
)
def create_order(
    db: Session = Depends(get_db),
    order: OrderSchema = Body(...)
):
    """
    Create Order

    This path operation create one order in the app.

    Parameters:
      - Request body parameter
        - order: Order

    Returns a json with the create order information:
      - id: UUID
      - order_number: int
      - user_id: str
      - name: str
      - phone_number: str
      - description: str
      - delivery_date: datetime
      - status: Optional[str]
      - created_at: Optional[datetime]
    """

    last_order = db.query(Order).order_by(
        Order.order_number.desc()).limit(1).first()

    increment_order_number = 0

    if not last_order:
        increment_order_number = 1
    else:
        increment_order_number = last_order.order_number + 1

    _order = Order(
        order_number=increment_order_number,
        user_id=order.user_id,
        name=order.name,
        phone_number=order.phone_number,
        description=order.description,
        delivery_date=order.delivery_date,
        status=order.status,
    )

    db.add(_order)
    db.commit()
    db.refresh(_order)

    return _order


# Update Order by ID
@order.put(
    path="/api/orders/{order_id}",
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK,
    summary="Update Order",
    tags=["Orders"]
)
def update_order(
    db: Session = Depends(get_db),
    order_id: str = Path(
        ...,
        title="Order ID",
        description="This is a Order ID.",
        example="efa1439c-a967-4b97-a5c0-7b4e42fe87a3"
    ),
    order: OrderSchema = Body(...)
):
    """
    Update Order

    This path operation update one order in the app.

    Parameters:
      - Request path parameter
        - order_id: UUID
      - Request body parameter
        - order: Order

    Returns a json with the update order information:
      - id: UUID
      - order_number: int
      - user_id: str
      - name: str
      - phone_number: str
      - description: str
      - delivery_date: datetime
      - status: Optional[str]
      - created_at: Optional[datetime]
    """

    _order = get_order(db, order_id)

    if _order:
        _order.user_id = order.user_id
        _order.name = order.name
        _order.phone_number = order.phone_number
        _order.description = order.description
        _order.delivery_date = order.delivery_date
        _order.status = order.status

        db.commit()

        return _order
    else:
        return HTTPException(status_code=404, detail="Order not found")


# Delete Order by ID
@order.delete(
    path="/api/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete Order",
    tags=["Orders"]
)
def delete_order(
    db: Session = Depends(get_db),
    order_id: str = Path(
        ...,
        title="Order ID",
        description="This is a Order ID.",
        example="efa1439c-a967-4b97-a5c0-7b4e42fe87a3"
    )
):
    """
    Delete Order

    This path operation delete one order in the app.

    Parameters:
      - Request path parameter
        - order_id: UUID

    Returns a json with the delete order information:
      - order_id: UUID
    """

    _order = get_order(db, order_id)

    if not _order:
        return HTTPException(status_code=404, detail="Order not found")

    db.delete(_order)
    db.commit()

    return {
        "order_id": order_id
    }
