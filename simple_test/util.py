from datetime import datetime

def sys_time() -> str:
    return datetime.now().strftime('%H:%M:%S')

def sys_date() -> str:
    return datetime.now().strftime('%Y-%m-%d')