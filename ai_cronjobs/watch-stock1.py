import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from lib.ai import run_structured_prompt
from lib.files import read_text, store_text
from lib.http import get_content_from_url
from lib.notifications import notify
from pydantic import BaseModel, Field

load_dotenv()

cfg = {
    "url": os.getenv("STOCK1_URL"),
    "symbol": os.getenv("STOCK1_SYMBOL"),
    "upper": float(os.getenv("STOCK1_UPPER")),
    "lower": float(os.getenv("STOCK1_LOWER")),
    "prompt": "Extract the current {symbol} stock value from this text: {content}",
    "data_file": "watch-stock1.dat",
    "llm_model": "gpt-4o",
}


class Stock(BaseModel):
    setup: str = Field(description="Stock information")
    symbol: str = Field(description="Stock symbol")
    value: float = Field(description="Current value of the stock")


def get_value_from_content(content, config) -> Stock:
    prompt = PromptTemplate(template=config["prompt"], input_variables=["content", "symbol"]).format(
        content=content, symbol=config["symbol"]
    )
    return run_structured_prompt(prompt, config["llm_model"], Stock)


def check_stock_value(config):
    content = get_content_from_url(config["url"])
    stock = get_value_from_content(content, config)

    if stock is None:
        print("Info not found.")
        return

    if stock.symbol != config["symbol"]:
        print(f"Symbol mismatch: {stock.symbol} != {config['symbol']}")
        return

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), config["data_file"])
    previous_value = read_text(file_path)
    print(f"Previous value: {previous_value}")
    print(f"Current value: {stock.value}")

    if previous_value != stock.value:
        store_text(file_path, stock.value)
        print(f"New stock value: {config['symbol']} {stock.value}")

        if stock.value > config["upper"]:
            print(f"{config['symbol']} stock: {stock.value} > {config['upper']}")
            notify(f"{config['symbol']} stock: {stock.value} > {config['upper']}")
        elif stock.value < config["lower"]:
            print(f"{config['symbol']} stock: {stock.value} < {config['lower']}")
            notify(f"{config['symbol']} stock: {stock.value} < {config['lower']}")
    else:
        print("No change detected.")


# ===================================================================
if __name__ == "__main__":
    check_stock_value(cfg)
