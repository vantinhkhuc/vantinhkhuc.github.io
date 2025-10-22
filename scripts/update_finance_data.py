"""
Script tự động lấy dữ liệu tài chính từ Fireant.vn
Cập nhật dữ liệu cho Module Finance
"""

import requests
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import os

class FireantScraper:
    """Class để lấy dữ liệu từ Fireant API"""
    
    BASE_URL = "https://restv2.fireant.vn"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
            'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoyMDYxMDkwNzI1LCJuYmYiOjE3NjEwOTA3MjUsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsInJvbGVzIiwiZW1haWwiLCJhY2NvdW50cy1yZWFkIiwiYWNjb3VudHMtd3JpdGUiLCJvcmRlcnMtcmVhZCIsIm9yZGVycy13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImZpbmFuY2UtcmVhZCIsInBvc3RzLXdyaXRlIiwicG9zdHMtcmVhZCIsInN5bWJvbHMtcmVhZCIsInVzZXItZGF0YS1yZWFkIiwidXNlci1kYXRhLXdyaXRlIiwidXNlcnMtcmVhZCIsInNlYXJjaCIsImFjYWRlbXktcmVhZCIsImFjYWRlbXktd3JpdGUiLCJibG9nLXJlYWQiLCJpbnZlc3RvcGVkaWEtcmVhZCJdLCJzdWIiOiIzOTViODBjZS1lY2M0LTRhMDktYTc5YS0yM2YyMDRiOWM2ODEiLCJhdXRoX3RpbWUiOjE3NjEwOTA3MjUsImlkcCI6Ikdvb2dsZSIsIm5hbWUiOiJodWZsaXQuY2xhc3Nyb29tQGdtYWlsLmNvbSIsInNlY3VyaXR5X3N0YW1wIjoiOGU0MDQxOTktODVhMi00YjI0LWE1NTItZmMyMGE2NjM4Y2FmIiwianRpIjoiOWFmYTJhOGE3NDk0YTZmMTE4Zjg1ZDFmY2ZjOTMwMWQiLCJhbXIiOlsiZXh0ZXJuYWwiXX0.XY5R0tCPmYJbULLB-VdooZ2EpydSN77rpSPwD4fud3O_tU-f2cIkLwcFXz4alWmXTUr5qrV4UbhihXY2z0HEQrcJ0O-P5CRAEFx1o29xO4Wzgg0UA4yCP79EoWMb_BGwxKSF102pUzCg5X3eJdPGSbeKboRdN-xwOB92NaG1BV1Frf8Y1asI1lyvZRCdS0ptxXozIfSf_YCKOIvS3TScbk5nNHc630VjpWFTCBQ7p1B0RPJFUHdshvb29_HZji8I3LQVqBL-bqV_rSqbwnwnKyoKyuJTcnYOigO91_gceTvacT9DG4Umre6upKZjT-AMMJwByNmqyQznLwXj_5-KAw'
        })
    
    def get_market_overview(self) -> Dict:
        """Lấy tổng quan thị trường"""
        try:
            # Lấy chỉ số thị trường chính
            indices = ['VNINDEX', 'HNXINDEX', 'UPCOMINDEX']
            markets = []
            
            for index in indices:
                url = f"{self.BASE_URL}/symbols/{index}/historical-quotes"
                params = {
                    'startDate': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
                    'endDate': datetime.now().strftime('%Y-%m-%d'),
                    'offset': 0,
                    'limit': 1
                }
                
                response = self.session.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        latest = data[0]
                        markets.append({
                            'name': self._format_index_name(index),
                            'value': latest.get('priceClose', 0),
                            'change': latest.get('priceChange', 0),
                            'changePercent': latest.get('priceChangePercent', 0),
                            'volume': latest.get('totalVolume', 0)
                        })
                
                time.sleep(0.5)  # Tránh quá tải server
            
            return {
                'lastUpdate': datetime.now().isoformat(),
                'markets': markets
            }
            
        except Exception as e:
            print(f"Lỗi khi lấy market overview: {e}")
            return None
    
    def get_top_movers(self, exchange: str = 'HOSE', limit: int = 5) -> Dict:
        """Lấy top cổ phiếu tăng/giảm mạnh"""
        try:
            url = f"{self.BASE_URL}/market/top-movers"
            params = {
                'exchange': exchange,
                'type': 1  # 1: gainers, 2: losers
            }
            
            gainers_response = self.session.get(url, params=params)
            params['type'] = 2
            losers_response = self.session.get(url, params=params)
            
            top_gainers = []
            top_losers = []
            
            if gainers_response.status_code == 200:
                gainers_data = gainers_response.json()
                for item in gainers_data[:limit]:
                    top_gainers.append({
                        'symbol': item.get('symbol', ''),
                        'name': item.get('organShortName', ''),
                        'price': item.get('lastPrice', 0),
                        'change': item.get('priceChange', 0),
                        'changePercent': item.get('priceChangePercent', 0),
                        'volume': item.get('totalVolume', 0)
                    })
            
            if losers_response.status_code == 200:
                losers_data = losers_response.json()
                for item in losers_data[:limit]:
                    top_losers.append({
                        'symbol': item.get('symbol', ''),
                        'name': item.get('organShortName', ''),
                        'price': item.get('lastPrice', 0),
                        'change': item.get('priceChange', 0),
                        'changePercent': item.get('priceChangePercent', 0),
                        'volume': item.get('totalVolume', 0)
                    })
            
            return {
                'topGainers': top_gainers,
                'topLosers': top_losers
            }
            
        except Exception as e:
            print(f"Lỗi khi lấy top movers: {e}")
            return None
    
    def get_stock_price_history(self, symbol: str, days: int = 30) -> List[Dict]:
        """Lấy lịch sử giá cổ phiếu"""
        try:
            url = f"{self.BASE_URL}/symbols/{symbol}/historical-quotes"
            params = {
                'startDate': (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d'),
                'endDate': datetime.now().strftime('%Y-%m-%d'),
                'offset': 0,
                'limit': days
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                candles = []
                
                for item in reversed(data):  # Đảo ngược để có thứ tự tăng dần
                    candles.append({
                        'time': datetime.fromtimestamp(item['date'] / 1000).strftime('%d/%m'),
                        'open': item.get('priceOpen', 0),
                        'high': item.get('priceHigh', 0),
                        'low': item.get('priceLow', 0),
                        'close': item.get('priceClose', 0),
                        'volume': item.get('totalVolume', 0)
                    })
                
                return candles
            
            return []
            
        except Exception as e:
            print(f"Lỗi khi lấy price history cho {symbol}: {e}")
            return []
    
    def get_financial_indicators(self, symbol: str) -> Dict:
        """Lấy chỉ số tài chính cơ bản"""
        try:
            url = f"{self.BASE_URL}/symbols/{symbol}/fundamental"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                return {
                    'pe': data.get('pe', 0),
                    'pb': data.get('pb', 0),
                    'eps': data.get('eps', 0),
                    'roe': data.get('roe', 0),
                    'roa': data.get('roa', 0),
                    'dividend': data.get('dividendYield', 0)
                }
            
            return {}
            
        except Exception as e:
            print(f"Lỗi khi lấy financial indicators cho {symbol}: {e}")
            return {}
    
    def get_financial_statements(self, symbol: str, statement_type: str = 'income') -> List[Dict]:
        """
        Lấy báo cáo tài chính
        statement_type: 'income', 'balance', 'cashflow'
        """
        try:
            type_mapping = {
                'income': 'INCOME_STATEMENT',
                'balance': 'BALANCE_SHEET',
                'cashflow': 'CASH_FLOW'
            }
            
            url = f"{self.BASE_URL}/symbols/{symbol}/full-financial-reports"
            params = {
                'type': type_mapping.get(statement_type, 'INCOME_STATEMENT'),
                'year': datetime.now().year,
                'quarter': 0  # 0 = yearly
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                return data
            
            return []
            
        except Exception as e:
            print(f"Lỗi khi lấy financial statements: {e}")
            return []
    
    def calculate_technical_indicators(self, candles: List[Dict]) -> Dict:
        """Tính toán các chỉ báo kỹ thuật đơn giản"""
        if not candles or len(candles) < 20:
            return {}
        
        closes = [c['close'] for c in candles]
        
        # Simple Moving Averages
        ma20 = sum(closes[-20:]) / 20 if len(closes) >= 20 else closes[-1]
        ma50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else closes[-1]
        
        # RSI (simplified)
        rsi = self._calculate_rsi(closes)
        
        # MACD (simplified)
        ema12 = self._calculate_ema(closes, 12)
        ema26 = self._calculate_ema(closes, 26)
        macd = ema12 - ema26
        signal = self._calculate_ema([macd], 9)
        
        return {
            'rsi': {
                'value': round(rsi, 2),
                'signal': 'Mua' if rsi < 30 else 'Bán' if rsi > 70 else 'Trung lập'
            },
            'macd': {
                'value': round(macd, 2),
                'signal': round(signal, 2),
                'histogram': round(macd - signal, 2),
                'trend': 'Tăng' if macd > signal else 'Giảm'
            },
            'ma20': round(ma20, 2),
            'ma50': round(ma50, 2),
            'ma200': round(sum(closes[-200:]) / 200, 2) if len(closes) >= 200 else round(closes[-1], 2),
            'bollinger': self._calculate_bollinger(closes),
            'stochastic': self._calculate_stochastic(candles)
        }
    
    def _calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """Tính RSI"""
        if len(prices) < period + 1:
            return 50.0
        
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100.0
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def _calculate_ema(self, prices: List[float], period: int) -> float:
        """Tính EMA"""
        if not prices:
            return 0.0
        
        multiplier = 2 / (period + 1)
        ema = prices[0]
        
        for price in prices[1:]:
            ema = (price * multiplier) + (ema * (1 - multiplier))
        
        return ema
    
    def _calculate_bollinger(self, prices: List[float], period: int = 20) -> Dict:
        """Tính Bollinger Bands"""
        if len(prices) < period:
            return {'upper': 0, 'middle': 0, 'lower': 0}
        
        recent = prices[-period:]
        sma = sum(recent) / period
        std = (sum((x - sma) ** 2 for x in recent) / period) ** 0.5
        
        return {
            'upper': round(sma + 2 * std, 2),
            'middle': round(sma, 2),
            'lower': round(sma - 2 * std, 2)
        }
    
    def _calculate_stochastic(self, candles: List[Dict], period: int = 14) -> Dict:
        """Tính Stochastic Oscillator"""
        if len(candles) < period:
            return {'k': 50, 'd': 50, 'signal': 'Trung lập'}
        
        recent = candles[-period:]
        closes = [c['close'] for c in recent]
        highs = [c['high'] for c in recent]
        lows = [c['low'] for c in recent]
        
        highest = max(highs)
        lowest = min(lows)
        current_close = closes[-1]
        
        if highest == lowest:
            k = 50
        else:
            k = ((current_close - lowest) / (highest - lowest)) * 100
        
        # Simple %D (3-period SMA of %K)
        d = k  # Simplified
        
        signal = 'Quá mua' if k > 80 else 'Quá bán' if k < 20 else 'Trung lập'
        
        return {
            'k': round(k, 2),
            'd': round(d, 2),
            'signal': signal
        }
    
    def _format_index_name(self, index: str) -> str:
        """Format tên chỉ số"""
        mapping = {
            'VNINDEX': 'VN-Index',
            'HNXINDEX': 'HNX-Index',
            'UPCOMINDEX': 'UPCOM'
        }
        return mapping.get(index, index)


class FinanceDataUpdater:
    """Class để cập nhật và lưu dữ liệu"""
    
    def __init__(self, output_dir: str = 'data/finance'):
        self.scraper = FireantScraper()
        self.output_dir = output_dir
        
        # Tạo thư mục nếu chưa có
        os.makedirs(output_dir, exist_ok=True)
    
    def update_dashboard(self):
        """Cập nhật dữ liệu dashboard"""
        print("📊 Đang cập nhật Dashboard...")
        
        # Lấy market overview
        market_data = self.scraper.get_market_overview()
        if not market_data:
            print("❌ Không thể lấy market overview")
            return
        
        # Lấy top movers
        movers = self.scraper.get_top_movers(limit=5)
        if movers:
            market_data.update(movers)
        
        # Lưu file
        output_file = os.path.join(self.output_dir, 'dashboard.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(market_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã cập nhật Dashboard -> {output_file}")
    
    def update_technical_analysis(self, symbol: str = 'VNM'):
        """Cập nhật phân tích kỹ thuật"""
        print(f"📈 Đang cập nhật Phân Tích Kỹ Thuật cho {symbol}...")
        
        # Lấy dữ liệu giá
        candles_1day = self.scraper.get_stock_price_history(symbol, days=60)
        candles_1week = self.scraper.get_stock_price_history(symbol, days=120)
        candles_1month = self.scraper.get_stock_price_history(symbol, days=365)
        
        if not candles_1day:
            print(f"❌ Không thể lấy dữ liệu cho {symbol}")
            return
        
        # Tính indicators
        indicators = self.scraper.calculate_technical_indicators(candles_1day)
        
        # Lấy thông tin cổ phiếu
        current_price = candles_1day[-1]['close'] if candles_1day else 0
        
        # Tạo analysis text
        analysis = self._generate_technical_analysis(current_price, indicators)
        
        data = {
            'symbol': symbol,
            'name': self._get_stock_name(symbol),
            'currentPrice': current_price,
            'timeframes': {
                '1day': candles_1day[-30:],  # 30 ngày gần nhất
                '1week': self._resample_to_weekly(candles_1week),
                '1month': self._resample_to_monthly(candles_1month)
            },
            'indicators': indicators,
            'analysis': analysis
        }
        
        # Lưu file
        output_file = os.path.join(self.output_dir, 'technical-analysis.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã cập nhật Phân Tích Kỹ Thuật -> {output_file}")
    
    def update_fundamental_analysis(self, symbol: str = 'VNM'):
        """Cập nhật phân tích cơ bản"""
        print(f"💰 Đang cập nhật Phân Tích Cơ Bản cho {symbol}...")
        
        # Lấy chỉ số tài chính
        indicators = self.scraper.get_financial_indicators(symbol)
        
        # Lấy báo cáo tài chính
        income_stmt = self.scraper.get_financial_statements(symbol, 'income')
        balance_sheet = self.scraper.get_financial_statements(symbol, 'balance')
        cashflow = self.scraper.get_financial_statements(symbol, 'cashflow')
        
        data = {
            'symbol': symbol,
            'name': self._get_stock_name(symbol),
            'sector': 'Đang cập nhật',
            'overview': {
                'marketCap': 'Đang cập nhật',
                'pe': indicators.get('pe', 0),
                'pb': indicators.get('pb', 0),
                'eps': indicators.get('eps', 0),
                'dividend': indicators.get('dividend', 0),
                'roe': indicators.get('roe', 0),
                'roa': indicators.get('roa', 0)
            },
            'incomeStatement': self._format_financial_statement(income_stmt, 'income'),
            'balanceSheet': self._format_financial_statement(balance_sheet, 'balance'),
            'cashFlow': self._format_financial_statement(cashflow, 'cashflow'),
            'analysis': self._generate_fundamental_analysis(indicators)
        }
        
        # Lưu file
        output_file = os.path.join(self.output_dir, 'fundamental-analysis.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã cập nhật Phân Tích Cơ Bản -> {output_file}")
    
    def update_macro_analysis(self):
        """Cập nhật phân tích vĩ mô"""
        print("🌍 Đang cập nhật Phân Tích Vĩ Mô...")
        
        # Dữ liệu vĩ mô thường lấy từ các nguồn khác (World Bank, GSO, etc.)
        # Đây là template cơ bản
        data = {
            'vietnam': {
                'gdp': {'value': '7.2%', 'trend': 'up', 'description': 'Tăng trưởng GDP'},
                'inflation': {'value': '3.8%', 'trend': 'stable', 'description': 'CPI'},
                'unemployment': {'value': '2.3%', 'trend': 'down', 'description': 'Tỷ lệ thất nghiệp'},
                'interest': {'value': '4.5%', 'trend': 'stable', 'description': 'Lãi suất cơ bản'},
                'exchange': {'value': '24,350', 'trend': 'up', 'description': 'VND/USD'},
                'fdi': {'value': '$28.5B', 'trend': 'up', 'description': 'Vốn FDI'}
            },
            'global': {
                'usgdp': {'value': '2.8%', 'trend': 'stable', 'description': 'US GDP'},
                'fedrate': {'value': '5.25-5.50%', 'trend': 'stable', 'description': 'Lãi suất Fed'},
                'oil': {'value': '$85.5', 'trend': 'up', 'description': 'Giá dầu WTI/thùng'},
                'gold': {'value': '$1,985', 'trend': 'up', 'description': 'Vàng/ounce'},
                'vix': {'value': '15.2', 'trend': 'down', 'description': 'Chỉ số biến động'}
            },
            'analysis': 'Kinh tế Việt Nam duy trì đà tăng trưởng tốt. Lạm phát được kiểm soát. Triển vọng tích cực.'
        }
        
        # Lưu file
        output_file = os.path.join(self.output_dir, 'macro-analysis.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã cập nhật Phân Tích Vĩ Mô -> {output_file}")
    
    def _resample_to_weekly(self, candles: List[Dict]) -> List[Dict]:
        """Chuyển đổi dữ liệu ngày thành tuần"""
        if not candles or len(candles) < 5:
            return candles
        
        weekly = []
        for i in range(0, len(candles), 5):
            week = candles[i:i+5]
            if week:
                weekly.append({
                    'time': f'T{len(weekly)+1}',
                    'open': week[0]['open'],
                    'high': max(c['high'] for c in week),
                    'low': min(c['low'] for c in week),
                    'close': week[-1]['close'],
                    'volume': sum(c['volume'] for c in week)
                })
        
        return weekly[-20:]  # 20 tuần gần nhất
    
    def _resample_to_monthly(self, candles: List[Dict]) -> List[Dict]:
        """Chuyển đổi dữ liệu ngày thành tháng"""
        if not candles or len(candles) < 20:
            return candles
        
        monthly = []
        for i in range(0, len(candles), 20):
            month = candles[i:i+20]
            if month:
                monthly.append({
                    'time': f'T{len(monthly)+1}',
                    'open': month[0]['open'],
                    'high': max(c['high'] for c in month),
                    'low': min(c['low'] for c in month),
                    'close': month[-1]['close'],
                    'volume': sum(c['volume'] for c in month)
                })
        
        return monthly[-12:]  # 12 tháng gần nhất
    
    def _get_stock_name(self, symbol: str) -> str:
        """Lấy tên công ty (có thể mở rộng)"""
        names = {
            'VNM': 'Vinamilk',
            'VIC': 'Vingroup',
            'HPG': 'Hòa Phát',
            'VCB': 'Vietcombank',
            'FPT': 'FPT Corporation'
        }
        return names.get(symbol, symbol)
    
    def _format_financial_statement(self, data: List, stmt_type: str) -> List[Dict]:
        """Format báo cáo tài chính"""
        # Đây là template - cần customize dựa trên cấu trúc thực tế của Fireant API
        formatted = []
        
        # Template cho 3 năm
        for i in range(3):
            year = datetime.now().year - i
            formatted.append({
                'year': str(year),
                'revenue': 0,
                'grossProfit': 0,
                'operatingIncome': 0,
                'netIncome': 0,
                'totalAssets': 0,
                'totalLiabilities': 0,
                'equity': 0,
                'operating': 0,
                'investing': 0,
                'financing': 0,
                'net': 0
            })
        
        return formatted
    
    def _generate_technical_analysis(self, price: float, indicators: Dict) -> str:
        """Tạo nhận định kỹ thuật"""
        signals = []
        
        if indicators.get('rsi', {}).get('signal') == 'Mua':
            signals.append('RSI cho tín hiệu mua')
        
        if indicators.get('macd', {}).get('trend') == 'Tăng':
            signals.append('MACD đang tăng')
        
        if price > indicators.get('ma20', 0):
            signals.append('Giá nằm trên MA20')
        
        if signals:
            return f"Xu hướng tích cực. {'. '.join(signals)}. Khuyến nghị: Theo dõi để mua."
        else:
            return "Xu hướng trung lập. Khuyến nghị: Đợi tín hiệu rõ ràng hơn."
    
    def _generate_fundamental_analysis(self, indicators: Dict) -> str:
        """Tạo nhận định cơ bản"""
        roe = indicators.get('roe', 0)
        pe = indicators.get('pe', 0)
        
        if roe > 15 and 0 < pe < 20:
            return "Công ty có hiệu suất tài chính tốt với ROE cao và P/E hợp lý. Khuyến nghị: MUA và NẮM GIỮ."
        elif roe > 10:
            return "Công ty có hiệu suất khá tốt. Khuyến nghị: THEO DÕI."
        else:
            return "Cần xem xét kỹ hơn các chỉ số tài chính. Khuyến nghị: THẬN TRỌNG."
    
    def update_all(self, symbols: List[str] = ['VNM']):
        """Cập nhật tất cả dữ liệu"""
        print("=" * 60)
        print("🚀 BẮT ĐẦU CẬP NHẬT DỮ LIỆU TÀI CHÍNH")
        print("=" * 60)
        
        try:
            self.update_dashboard()
            time.sleep(2)
            
            for symbol in symbols:
                self.update_technical_analysis(symbol)
                time.sleep(2)
                
                self.update_fundamental_analysis(symbol)
                time.sleep(2)
            
            self.update_macro_analysis()
            
            print("=" * 60)
            print("✅ HOÀN THÀNH CẬP NHẬT")
            print("=" * 60)
            
        except Exception as e:
            print(f"❌ Lỗi: {e}")


# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    # Khởi tạo updater
    updater = FinanceDataUpdater(output_dir='data/finance')
    
    # Danh sách cổ phiếu cần theo dõi
    watchlist = ['VNM', 'VIC', 'HPG', 'VCB', 'FPT']
    
    # Cập nhật tất cả
    updater.update_all(symbols=watchlist[:1])  # Chỉ update 1 mã để test
    
    print("\n📝 Lưu ý:")
    print("- Dữ liệu đã được lưu vào thư mục 'data/finance/'")
    print("- Bạn có thể schedule script này chạy định kỳ với cron hoặc GitHub Actions")
    print("- API Fireant có thể thay đổi, cần kiểm tra và cập nhật thường xuyên")
