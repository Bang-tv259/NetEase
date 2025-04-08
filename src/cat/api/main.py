from __future__ import annotations

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cat.api.routers import net_ease
from cat.common.config import AppConfig


config = AppConfig()

app = FastAPI(
    title="NetEase Product",
    description="Handle Gross to Net.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(net_ease.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.host, port=config.port, reload=True)
