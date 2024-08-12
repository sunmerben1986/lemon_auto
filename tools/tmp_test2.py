import time
import threading

def singleton(cls):
    _instance = {}
    _lock = threading.Lock()
    def wraper(*args, **kwargs):
        if cls not in _instance:
            with _lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wraper

@singleton
class Config:
    def __init__(self) -> None:
        time.sleep(1)

    def __getattr__(self, attr):
        return attr