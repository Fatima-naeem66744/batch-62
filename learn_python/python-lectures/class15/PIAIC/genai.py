from typing import Any


class commulative_average():
    def __init__(self):
        self.data = []
    def __call__(self , new_value) -> Any:
        self.data.append(new_value)
        print(self.data)
        return sum(self.data) / len(self.data)  # [12]  [12 / 1]
result = commulative_average()

result(12)  
result(13)  
result(14)  



        
        