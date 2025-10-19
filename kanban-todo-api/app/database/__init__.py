from .connection import Base, engine, get_db, create_tables, SessionLocal
from .models import User, Board, Task, StatusEnum, PriorityEnum
from .repository import UserRepository, BoardRepository, TaskRepository

# Tạo các repository instances để sử dụng trong routers
user_repository = UserRepository()
board_repository = BoardRepository()
task_repository = TaskRepository()

__all__ = [
    "Base", "engine", "get_db", "create_tables", "SessionLocal",
    "User", "Board", "Task", "StatusEnum", "PriorityEnum", 
    "UserRepository", "BoardRepository", "TaskRepository",
    "user_repository", "board_repository", "task_repository"
]
