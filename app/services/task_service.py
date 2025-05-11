from typing import List, Optional
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.orm import Session
from repository.task_repository import ToDoRepository

