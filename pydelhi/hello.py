from datetime import datetime
from .date_helper import get_month


def say_hello(name: str, dt: datetime) -> str:
    month = get_month(dt)
    return f"Hello {name}!. Welcome to Pydelhi {month} talk"
