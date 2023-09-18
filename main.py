from fastapi import FastAPI
import uvicorn


if __name__ == '__main__':

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello Cloud"}

    @app.get("/add/{num1}/{num2}")
    async def add(num1: int, num2: int):
        """Add two numbers together"""

        total = num1 + num2
        return {"total": total}

    uvicorn.run(app, port=8080, host='0.0.0.0')