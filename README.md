# MonteCarloPortfolioOptimization

## Goal
Using Monte Carlo Simulation for Portfolio Optimization by assigning random weights to each Sector SPDR ETF.
Iterating 1000 times to increase the accuracy for portfolio optimization
Collecting portfolios returns and standard deviation to calculate Sharpe Ratio

## Metric
Sharpe Ratio (risk adjusted return): the ratio of reward (Portolfio's Returns) to risks (Portfolio's Volatility), normally annualized.
The Sharpe Ratio gives market-participants the confidence to apply leverage.


### Code

Created 4 modules
- `config.py`: Define Global Variable for Paths
- `main.py`: Monte Carlo Simulation and calculating the max annualized sharpe-ratio
- `data.py`: Extract the Adjusted-Closing Price for each sector ETF

### Install
Install the following Python libraries

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [YFinance](https://pypi.org/project/yfinance/)

### Run

In a terminal or command window, navigate to the top-level project directory `MonteCarloPorfolioOptimization/` (that contains this README) and run the following command:

```bash
pip install --upgrade pip && pip install -r requirements.txt
``` 

## Data: Sector SPDR ETFs
[Collecting Sector SPDR ETFs](https://www.sectorspdr.com/sectorspdr/)

- `SPY`: S&P 500 Index Fund 
- `XLF`: Financial
- `XLY`: Consumer Discretionary
- `XLK`: Technology
- `XLB`: Materials
- `XLI`: Industrials
- `XLE`: Energy
- `XLU`: Utilites
- `XLV`: Health Care
- `XLP`: Consumer Staples