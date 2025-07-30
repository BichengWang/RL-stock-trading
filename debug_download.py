#!/usr/bin/env python3
"""
Debug script to understand the data download issue
"""

import pandas as pd
import yfinance as yf

def debug_download():
    """Debug the download process"""
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    ticker_list = ["AAPL", "MSFT", "GOOGL"]
    
    print("=== Testing individual downloads ===")
    for tic in ticker_list:
        print(f"\nDownloading {tic}...")
        temp_df = yf.download(tic, start=start_date, end=end_date, auto_adjust=False)
        print(f"Shape: {temp_df.shape}")
        print(f"Columns: {temp_df.columns.tolist()}")
        print(f"Index: {temp_df.index[:5]}")
        
        # Reset index
        temp_df = temp_df.reset_index()
        print(f"After reset_index - Columns: {temp_df.columns.tolist()}")
        print(f"Sample data:")
        print(temp_df.head(3))
        print("-" * 50)
    
    print("\n=== Testing concatenation ===")
    data_df = pd.DataFrame()
    for tic in ticker_list:
        temp_df = yf.download(tic, start=start_date, end=end_date, auto_adjust=False)
        temp_df = temp_df.reset_index()
        temp_df["tic"] = tic
        data_df = pd.concat([data_df, temp_df], ignore_index=True)
        print(f"After adding {tic}: Shape = {data_df.shape}")
    
    print(f"\nFinal DataFrame:")
    print(f"Shape: {data_df.shape}")
    print(f"Columns: {data_df.columns.tolist()}")
    print(f"Sample data:")
    print(data_df.head())

if __name__ == "__main__":
    debug_download() 