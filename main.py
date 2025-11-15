from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/bye/{name}/{city}")
async def say_hello(name: str, city: str):
    return {"message": f"goodbye {name} from {city}"}

