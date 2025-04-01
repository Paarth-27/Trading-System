from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.models import Trade
from app.database import get_db
from app.real_time_data import simulate_stock_updates
import json
import asyncio

app = FastAPI()

@app.post("/trades/")
def add_trade(trade: Trade, db: Session = Depends(get_db)):
    new_trade = Trade(**trade.dict())
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade

@app.get("/trades/")
def get_trades(ticker: str = None, db: Session = Depends(get_db)):
    query = db.query(Trade)
    if ticker:
        query = query.filter(Trade.ticker == ticker)
    return query.all()

# WebSocket Implementation for Real-Time Stock Price Updates
@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        async for stock_prices in simulate_stock_updates():
            data = json.dumps(stock_prices)
            await websocket.send_text(data)
    except WebSocketDisconnect:
        pass
