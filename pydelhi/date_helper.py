from datetime import datetime


def get_month(dt: datetime) -> str:
    return dt.strftime("%B")
