from langchain_core.tools import tool
from pydantic import BaseModel, Field
from client import TWSEClient

twse = TWSEClient()

# Schema for single stock queries to ensure strict input validation
class StockInput(BaseModel):
    stock_id: str = Field(description="A 4-digit Taiwan stock ticker symbol, e.g., '2330'.")

# Schema for comparative analysis involving multiple entities
class CompareInput(BaseModel):
    stock_ids: list[str] = Field(description="A list of 4-digit ticker symbols, e.g., ['2330', '2317'].")

@tool(args_schema=StockInput)
def fetch_stock_basic_info(stock_id: str):
    """
    Retrieves the latest daily trading OHLCV data for a specific Taiwan stock.
    """
    try:
        res = twse.get_stock_daily_detail(stock_id)
        if isinstance(res, dict):
            return f"最新交易日個股行情 ({stock_id}): {res}"
        return f"查詢失敗：格式錯誤 ({type(res)})"
    except Exception as e:
        return f"查詢失敗：{str(e)}"

@tool(args_schema=CompareInput)
def compare_stocks_performance(stock_ids: list[str]):
    """
    Compares market performance for multiple Taiwan stocks.
    """
    results = []
    for sid in stock_ids:
        try:
            data = twse.get_stock_daily_detail(sid)
            results.append(f"{sid}: {data}")
            # if isinstance(data, dict):
            #     results.append(f"{sid}: {data}")
            # else:
            #     results.append(f"{sid}: 查詢失敗 (非預期格式)")
        except Exception:
            results.append(f"{sid}: 查詢失敗 (API 錯誤)")
    return "\n".join(results)

@tool
def fetch_market_status(query: str = None):
    """
    Retrieves the latest overall TAIEX market summary and volume.
    """
    try:
        res = twse.get_market_summary()
        if isinstance(res, dict):
            return f"最新大盤摘要: {res}"
        return "查詢失敗：大盤格式異常"
    except Exception as e:
        return f"查詢失敗：{str(e)}"

tools = [
    fetch_stock_basic_info,
    compare_stocks_performance,
    fetch_market_status
]