from fastapi import FastAPI,Depends
from shemsw import Product
from database import engine,SessionLocal,Base
from sqlalchemy.orm import Session

app = FastAPI()
from model import User
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:

        db.close_all()


@app.post("/")
async def root(Products:Product,db:Session = Depends(get_db)):
    print(Products)
    new_blog = User(name = Products.name ,category = Products.category,price=Products.price)
    print(new_blog,'new_bolg')
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/Products")
async def getdata_(db:Session = Depends(get_db)):
    Product_type = db.query(User).all()
    return Product_type

@app.get("/Products/{id}")
async def getdata_for_specific(id,db:Session = Depends(get_db)):
    Product_type = db.query(User).filter(User.id == id).first()
    return Product_type

@app.put("/Products/{id}")
async def add_employees(id,Products:Product,db:Session = Depends(get_db)):
    blog_ = db.query(User).filter(User.id == id).update({'price': Products.price})
    db.commit()
    return id
@app.delete("/Products/{id}")
async def delete_item(id: int):
    db = SessionLocal()
    db_item = db.query(User).filter(User.id == id).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}