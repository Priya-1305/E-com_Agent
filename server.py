from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uagents import Agent, Context
import uuid  # For generating unique order IDs

app = FastAPI()

# Define the data models
class ProductRecommendationRequest(BaseModel):
    user_id: str

class ProductRecommendationResponse(BaseModel):
    products: list[str]

class OrderRequest(BaseModel):
    user_id: str
    product_ids: list[str]

class OrderResponse(BaseModel):
    status: str
    order_id: str
    order_details: dict

class CustomerSupportRequest(BaseModel):
    user_id: str
    query: str

class CustomerSupportResponse(BaseModel):
    response: str

# Initialize the agent
ecommerce_agent = Agent(name="ecommerce_agent", seed="ecommerce recovery phrase")

# Define endpoints
@app.post("/recommend-products")
async def recommend_products(request: ProductRecommendationRequest):
    # Simulate interaction with the agent
    products = ["Product A", "Product B", "Product C"]
    response = ProductRecommendationResponse(products=products)
    return response

@app.post("/process-order")
async def process_order(request: OrderRequest):
    order_id = str(uuid.uuid4())  # Generate a unique order ID
    order_details = {"user_id": request.user_id, "products": request.product_ids}
    response = OrderResponse(
        status="Order processed",
        order_id=order_id,  # Include the generated order ID
        order_details=order_details
    )
    return response

@app.post("/customer-support")
async def customer_support(request: CustomerSupportRequest):
    response = CustomerSupportResponse(response="Support response to query")
    return response

# Run the FastAPI server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
