# Trading-System

## Overview
This project implements a basic trading system with the following components:

1. **REST API** - Built using FastAPI and PostgreSQL for managing trade operations.
2. **Real-Time Data Processing** - Simulated stock price updates via WebSocket.
3. **Cloud Integration (AWS)** - AWS Lambda function to analyze trade data stored in S3.
4. **Optional** - Algorithmic Trading Simulation using a Moving Average Crossover strategy.

## Features

### 1. REST API Development
- `POST /trades/` - Add trade details (e.g., ticker, price, quantity, side (buy/sell), timestamp).
- `GET /trades/` - Retrieve trade records, optionally filtered by ticker or date range.

### 2. Real-Time Data Processing
- WebSocket connection (`/ws/`) simulates stock price updates.
- Each stock price fluctuates by a random factor (within a 2% range) every second.

### 3. Cloud Integration with AWS
- **Lambda Function**: Fetches trade data from an S3 bucket for a given date, analyzes total traded volume and average price, and stores the analysis result back to S3.

### 4. Algorithmic Trading Simulation (Optional)
- **Moving Average Crossover Strategy**: A simple strategy that buys when the 50-day moving average crosses above the 200-day moving average, and sells when it crosses below.

## Requirements
- Python 3.8+
- FastAPI
- PostgreSQL or MongoDB
- Boto3 (for AWS integration)
- Pandas
- Celery and Redis (for background tasks, optional)
- WebSocket for real-time communication

## Setup Instructions
### 1. Install Dependencies

```bash
pip install -r requirements.txt
