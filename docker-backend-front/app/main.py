# from typing import Union

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# import time

# app = FastAPI()

# origins = ["*"]

# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=origins,
# 	allow_credentials=True,
# 	allow_methods=["*"],
# 	allow_headers=["*"],
# )

# @app.get("/")
# def read_root():
#     return {"Hello world": f"{time.time()}"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello():
    return {"flask Hello world": time.time()}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8001')