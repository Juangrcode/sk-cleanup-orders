# Python
import uuid
from enum import Enum
from datetime import datetime

# SqlAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, DateTime, Enum

# Config DB
from config.db import Base


class StatusMode(Enum):
    received = "received"
    inProcess = "inProcess"
    finish = "finish"


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    order_number = Column(
        Integer,
        nullable=False
    )
    user_id = Column(
        String,
        nullable=False
    )
    name = Column(
        String,
        nullable=False
    )
    phone_number = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )
    delivery_date = Column(
        DateTime,
        nullable=False,
        default=datetime.now
    )
    status = Column(
        String,
        nullable=False,
        default=StatusMode.received
    )
    created_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )
