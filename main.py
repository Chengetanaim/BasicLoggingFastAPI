from fastapi import FastAPI, HTTPException, status, Response
import logging

from app.schemas import Product, ProductCreate, ProductUpdate

app = FastAPI()

logger = logging.getLogger(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

products = []


def fetch_product(id:int):
    for product in products:
        if product['id'] == id:
            return product
    return None


@app.post('/', status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(product:ProductCreate):
    try:
        kkk
        product = product.model_dump()
        product['id'] = len(products) + 1
        products.append(product)
        return product
    
    except Exception as e:
        logger.error(f'An unexpexted error occured while creating the product, {str(e)}')
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An unexpexted error occured while creating the product')


@app.get('/', response_model=list[Product])
def get_products():
    try:
        getproductserror
        return products
    
    except Exception as e:
        logger.error(f'An unexpexted error occured while getting products, {str(e)}')
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An unexpexted error occured while getting products')
    


@app.get('/{id}', response_model=Product)
def get_product(id:int):
    try:
        getproducterror
        product = fetch_product(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
        return product
    
    except Exception as e:
        logger.error(f'An unexpexted error occured while getting the product, {str(e)}')
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An unexpexted error occured while getting the product')


@app.put('/id', status_code=status.HTTP_202_ACCEPTED, response_model=Product)
def update_product(id:int, product_update:ProductUpdate):
    try:
        updateproducterror
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
    
    except Exception as e:
        logger.error(f'An unexpexted error occured while updating the product, {str(e)}')
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An unexpexted error occured while updating the product')


@app.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int):
    try:
        deleteproducterror
        product = fetch_product(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
        products.remove(product)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        logger.error(f'An unexpexted error occured while deleting the product, {str(e)}')
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An unexpexted error occured while deleting the product')