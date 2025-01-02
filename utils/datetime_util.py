from datetime import datetime

def sys_time() -> str:
    return datetime.now().strftime('%H:%M:%S')

def sys_date() -> str:
    return datetime.now().strftime('%Y-%m-%d')

def date_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def date_time_full() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')