import time
import ctypes

def disable_keyboard():
    # Load the user32.dll library
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    user32.BlockInput(True)

def enable_keyboard():
    user32 = ctypes.WinDLL('user32', use_last_error=True)    
    # Enable the keyboard
    user32.BlockInput(False)


