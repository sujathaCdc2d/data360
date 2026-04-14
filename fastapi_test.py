from fastapi import FastAPI

# 1. Create an instance of FastAPI
app = FastAPI()

# 2. Define a path operation (route)
@app.get("/")
def read_root():
    # 3. Return content (automatically converted to JSON)
    return {"message": "Hello World"}
