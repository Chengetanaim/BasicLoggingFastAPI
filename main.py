from fastapi import FastAPI, HTTPException, status, Response
from app.schemas import Product, ProductCreate, ProductUpdate

app = FastAPI()

products = []


def fetch_product(id:int):
    for product in products:
        if product['id'] == id:
            return product
    return None


@app.post('/', status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(product:ProductCreate):
    product = product.model_dump()
    product['id'] = len(products) + 1
    products.append(product)
    return product


@app.get('/', response_model=list[Product])
def get_products():
    return products


@app.get('/{id}', response_model=Product)
def get_product(id:int):
    product = fetch_product(id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product


@app.put('/id', status_code=status.HTTP_202_ACCEPTED, response_model=Product)
def update_product(id:int, product_update:ProductUpdate):
    product = fetch_product(id)
    
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    if product_update.name is not None:
        product['name'] = product_update.name

    if product_update.description is not None:
        product['description'] = product_update.description

    if product_update.price is not None:
        product['price'] = product_update.price

    if product_update.status is not None:
        product['status'] = product_update.status

    return product


@app.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int):
    product = fetch_product(id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    products.remove(product)
    return Response(status_code=status.HTTP_204_NO_CONTENT)