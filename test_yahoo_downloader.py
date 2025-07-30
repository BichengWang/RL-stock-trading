#!/usr/bin/env python3
"""
Test script for YahooDownloader to verify the fixes work correctly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rl.marketdata.yahoodownloader import YahooDownloader

def test_yahoo_downloader():
    """Test the YahooDownloader with a small dataset."""
    print("Testing YahooDownloader...")
    
    # Test parameters
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    ticker_list = ["AAPL", "MSFT", "GOOGL"]
    
    try:
        # Create downloader
        downloader = YahooDownloader(
            start_date=start_date,
            end_date=end_date,
            ticker_list=ticker_list
        )
        
        # Fetch data
        print(f"Downloading data for {ticker_list} from {start_date} to {end_date}...")
        data = downloader.fetch_data()
        
        # Check results
        print(f"\n✅ SUCCESS!")
        print(f"DataFrame shape: {data.shape}")
        print(f"Columns: {data.columns.tolist()}")
        print(f"Date range: {data['date'].min()} to {data['date'].max()}")
        print(f"Tickers: {data['tic'].unique().tolist()}")
        print(f"Sample data:")
        print(data.head())
        
        # Verify expected columns
        expected_columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'tic', 'day']
        missing_columns = [col for col in expected_columns if col not in data.columns]
        
        if missing_columns:
            print(f"❌ WARNING: Missing columns: {missing_columns}")
        else:
            print(f"✅ All expected columns present")
            
        # Verify data quality
        print(f"Missing values: {data.isnull().sum().sum()}")
        print(f"Data types: {data.dtypes.to_dict()}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_yahoo_downloader()
    if success:
        print("\n🎉 Test passed! YahooDownloader is working correctly.")
    else:
        print("\n💥 Test failed! There are still issues to fix.")
        sys.exit(1) 