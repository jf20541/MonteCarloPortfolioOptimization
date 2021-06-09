import pandas as pd
import yfinance as yf

if __name__ == "__main__":
    df = yf.download(
        "XLF XLY XLK XLB XLI XLE XLU XLV XLP SPY", start="2020-04-01", end="2021-04-02"
    )
    df = df["Adj Close"]
    df.to_csv("../inputs/train.csv")