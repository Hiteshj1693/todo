from typing import List, Optional, Type
from datetime import datetime
from pydantic import UUID4
from sqlalchemy.orm import Session
from model.task import Task
from schema.task import ToDoCreateIn, ToDoOut, ToDoUpdateIn 