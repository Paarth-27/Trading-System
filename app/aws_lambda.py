import boto3
import pandas as pd

def analyze_trade_data(date: str):
    s3_client = boto3.client('s3')
    bucket_name = "your-bucket-name"
    file_key = f"{date}/trades.csv"
    
    # Fetch the trade data CSV from S3
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    df = pd.read_csv(obj['Body'])

    # Calculate total volume and average price per stock
    analysis = df.groupby('ticker').agg({'quantity': 'sum', 'price': 'mean'}).reset_index()

    # Save the analysis result back to S3
    output_key = f"{date}/analysis_{date}.csv"
    analysis.to_csv(f"/tmp/{output_key}", index=False)
    s3_client.upload_file(f"/tmp/{output_key}", bucket_name, output_key)

    return {"message": "Analysis completed", "file": output_key}
