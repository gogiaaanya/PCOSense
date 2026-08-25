from fastapi import FastAPI

app = FastAPI(title="PCOSense API")


@app.get("/")
def home():
    return {
        "message": "PCOSense backend is running!"
    }