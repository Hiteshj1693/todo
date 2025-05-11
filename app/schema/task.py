from pydantic import BaseModel, Field, UUID4, field_validator
from typing import Optional, List
from datetime import datetime, date
from enum import Enum

class ToDoCreateIn(BaseModel):
    pass

class ToDoOut(BaseModel):
    pass

class ToDoUpdateIn(BaseModel):
    pass