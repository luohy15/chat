import time
from datetime import datetime

def get_unix_timestamp() -> int:
    """Get current time as 13-digit unix timestamp (milliseconds)"""
    return int(time.time() * 1000)

def get_iso8601_timestamp() -> str:
    localtime = time.localtime()
    offset = time.strftime("%z", localtime)
    offset_with_colon = f"{offset[:3]}:{offset[3:]}"
    formatted_time = time.strftime(f"%Y-%m-%dT%H:%M:%S{offset_with_colon}", localtime)
    return formatted_time
