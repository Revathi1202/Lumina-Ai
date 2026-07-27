from fastapi import FastAPI

app = FastAPI(
    title="MCP Gateway"
)


@app.get("/")
async def root():
    return {
        "message": "MCP Gateway Running"
    }