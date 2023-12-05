from pydantic import BaseModel, Field

class ModelaPost1(BaseModel):
  id: str = Field(default='X')
  nama: str = Field(default='X')
  slug: str = Field(default='X')
  urut: int = Field(default=-1)
  status_tampil: int = Field(default=1)
  
  