from typing import Any
import time 

class ExecutiveClass: 
    def __init__(self, func):
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()  # Start timer
        result = self.func(*args, **kwargs)  # Call the function
        end = time.perf_counter()  # End timer
        print(f"Function {self.func.__name__} executed in {(end-start):.4f} seconds")
        return result


