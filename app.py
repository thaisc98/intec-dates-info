from fastapi import FastAPI
from date_timee import DateTimee

app = FastAPI()
date_timee = DateTimee();

@app.get("/healthcheck")
async def root():
    return {"status": "Up and Adm Config."}

@app.get("/datetime/dominican-republic")
async def get_date_time():
   return  { "result": date_timee.dateTimeDO() }