import threading

_lock = threading.Lock()
_ROBOT_ACTIVE = False

def ligar():
    global _ROBOT_ACTIVE
    with _lock:
        _ROBOT_ACTIVE = True

def desligar():
    global _ROBOT_ACTIVE
    with _lock:
        _ROBOT_ACTIVE = False

def status():
    with _lock:
        return _ROBOT_ACTIVE
