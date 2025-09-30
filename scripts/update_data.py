# scripts/update_data.py
import requests
import json
import os
from datetime import datetime

# API endpoints (ví dụ)
VIETSTOCK_API = "https://api.vietstock.vn/data"
NEWS_API = "https://newsapi.org/v2/everything"

def fetch_stock_data():
    """Lấy dữ liệu cổ phiếu từ API"""
    try:
        # Ví dụ với VietStock API (cần đăng ký API key)
        headers = {
            'Authorization': f'Bearer {os.getenv("VIETSTOCK_API_KEY")}'
        }
        
        stocks = ['VNM', 'VIC', 'VCB', 'HPG', 'FPT', 'MSN']
        stock_data = []
        
        for symbol in stocks:
            response = requests.get(
                f"{VIETSTOCK_API}/stock/{symbol}",
                headers=headers
            )
            if response.status_code == 200:
                data = response.json()
                stock_data.append({
                    'symbol': symbol,
                    'price': data.get('price'),
                    'change': data.get('change'),
                    'volume': data.get('volume'),
                    'timestamp': datetime.now().isoformat()
                })
        
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return []

def fetch_vn_index():
    """Lấy dữ liệu VN-Index"""
    try:
        response = requests.get(f"{VIETSTOCK_API}/index/VNINDEX")
        if response.status_code == 200:
            data = response.json()
            return {
                'value': data.get('value'),
                'change': data.get('change'),
                'timestamp': datetime.now().isoformat()
            }
    except Exception as e:
        print(f"Error fetching VN-Index: {e}")
        return {}

def fetch_news():
    """Lấy tin tức từ NewsAPI hoặc RSS feeds"""
    try:
        # Sử dụng NewsAPI (miễn phí cho dev)
        params = {
            'apiKey': os.getenv('NEWS_API_KEY'),
            'q': 'vietnam OR chứng khoán OR tài chính',
            'language': 'vi',
            'sortBy': 'publishedAt',
            'pageSize': 10
        }
        
        response = requests.get(NEWS_API, params=params)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return [{
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'publishedAt': article['publishedAt']
            } for article in articles]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def fetch_macro_data():
    """Lấy dữ liệu vĩ mô"""
    try:
        # Có thể dùng World Bank API, IMF API, hoặc scrape từ các nguồn
        macro_data = {
            'vietnam': {
                'gdp_growth': 6.8,
                'inflation': 3.2,
                'usd_rate': 24850,
                'reserves': 112
            },
            'world': {
                'fed_rate': 5.25,
                'oil_price': 87.5,
                'gold_price': 2145,
                'bitcoin': 68250
            },
            'timestamp': datetime.now().isoformat()
        }
        return macro_data
    except Exception as e:
        print(f"Error fetching macro data: {e}")
        return {}

def save_data(data, filename):
    """Lưu dữ liệu vào file JSON"""
    os.makedirs('data', exist_ok=True)
    with open(f'data/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("Starting data update...")
    
    # Lấy và lưu dữ liệu cổ phiếu
    stock_data = fetch_stock_data()
    if stock_data:
        save_data(stock_data, 'stocks.json')
        print(f"Updated {len(stock_data)} stocks")
    
    # Lấy và lưu VN-Index
    vnindex = fetch_vn_index()
    if vnindex:
        save_data(vnindex, 'vnindex.json')
        print("Updated VN-Index")
    
    # Lấy và lưu tin tức
    news = fetch_news()
    if news:
        save_data(news, 'news.json')
        print(f"Updated {len(news)} news articles")
    
    # Lấy và lưu dữ liệu vĩ mô
    macro = fetch_macro_data()
    if macro:
        save_data(macro, 'macro.json')
        print("Updated macro data")
    
    print("Data update completed!")

if __name__ == "__main__":
    main()
