
import uvicorn
from config import get_config
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title=str(get_config().project_title),
    docs_url="/api/docs",
)
app.add_middleware(
    CORSMiddleware, allow_headers=["*"], allow_origins=["*"], allow_methods=["*"]
)

@app.get("/health_check")
def read_root_health_check():
    return {"data": "success!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8000,
    )
