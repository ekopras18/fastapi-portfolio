from enum import Enum

class Category(str, Enum):
  def __str__(self):
    return str(self.value)
  
  gov = "Government"
  priv = "Private Project"
  learn = "Self-directed learning"