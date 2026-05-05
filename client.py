import requests

class TWSEClient:    
    @staticmethod
    def _fetch_data(endpoint):
        url = f"https://openapi.twse.com.tw/v1{endpoint}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RuntimeError(f"TWSE API connection failed: {str(e)}")

    def get_stock_daily_detail(self, stock_id):
        data = self._fetch_data(f"/exchangeReport/STOCK_DAY_AVG_ALL")
        target = next((item for item in data if item.get('Code') == stock_id), None)
        if target:
            return {
                "股票代碼": target.get('Code'),
                "股票名稱": target.get('Name'),
                "收盤價": target.get('ClosingPrice'),
                "月平均價": target.get('MonthlyAveragePrice')
            }

        # if isinstance(data, dict) and data.get('data'):
        #     latest = data['data'][-1]
        #     return {
        #         "股票代碼": latest.get('Code'),
        #         "股票名稱": latest.get('Name'),
        #         "收盤價": latest.get('ClosingPrice'),
        #         "月平均價": latest.get('MonthlyAveragePrice')
        #     }
        
        raise ValueError(f"No daily data found for stock ID {stock_id}")

    def get_market_summary(self):
        data = self._fetch_data("/exchangeReport/FMTQIK")
        if isinstance(data, list) and len(data) > 0:
            return data[-1]
        raise ValueError("Market summary is currently unavailable")