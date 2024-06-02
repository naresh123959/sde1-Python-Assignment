from pydantic import BaseModel,validator,Field
class Product(BaseModel):
    name:str
    category: str
    price:float
    def Name_(cls, v):
        if v in '' and v in 'string':
            raise ValueError(f"Please enter vaild name , not {v}")


        return v
    class Config:
        orm_model = True