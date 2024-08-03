from pydantic import BaseModel
from uagents import Agent, Context

class ProductRecommendationRequest(BaseModel):
    user_id: str

class ProductRecommendationResponse(BaseModel):
    products: list[str]

class OrderRequest(BaseModel):
    user_id: str
    product_ids: list[str]

class OrderResponse(BaseModel):
    status: str
    order_details: dict

class CustomerSupportRequest(BaseModel):
    user_id: str
    query: str

class CustomerSupportResponse(BaseModel):
    response: str

ecommerce_agent = Agent(name="ecommerce_agent", seed="ecommerce recovery phrase")

@ecommerce_agent.on_message(model=ProductRecommendationRequest)
async def recommend_products(ctx: Context, message: ProductRecommendationRequest):
    # Logic to recommend products
    products = ["Product A", "Product B", "Product C"]
    response = ProductRecommendationResponse(products=products)
    ctx.send(message.sender, response)

@ecommerce_agent.on_message(model=OrderRequest)
async def process_order(ctx: Context, message: OrderRequest):
    order_details = {"user_id": message.user_id, "products": message.product_ids}
    # Logic to process the order
    response = OrderResponse(status="Order processed", order_details=order_details)
    ctx.send(message.sender, response)

@ecommerce_agent.on_message(model=CustomerSupportRequest)
async def customer_support(ctx: Context, message: CustomerSupportRequest):
    query = message.query
    # Logic to handle customer support queries
    response = CustomerSupportResponse(response="Support response to query")
    ctx.send(message.sender, response)

@ecommerce_agent.on_interval(period=60.0)  # Every 60 seconds
async def check_inventory(ctx: Context):
    # Logic to check and update inventory
    ctx.logger.info("Checking inventory...")

if __name__ == "__main__":
    ecommerce_agent.run()
