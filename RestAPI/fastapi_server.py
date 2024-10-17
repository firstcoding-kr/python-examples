#!/usr/bin/env python3
# 모듈설치: pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()
students = []

@app.on_event("startup")
async def on_startup():
    print('서버 시작')

# http://localhost/
@app.get("/")
async def get_some_data():
    return {'some': 'data'}

# http://localhost/students/1
@app.get("/students/{id}")
async def get_some_data(id):
    return {'id': id}

@app.on_event("shutdown")
async def shutdown_event():
    print('서버 종료')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
