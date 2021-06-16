# MonteCarloPortfolioOptimization

## Objective
Using Monte Carlo Simulation for Portfolio Optimization by assigning random weights to each Sector SPDR ETF\
Iterating n-times to increase the accuracy for portfolio optimization\
Collecting portfolio's returns and standard deviation to calculate Portfolio's Sharpe-Ratio

## Metric
Sharpe Ratio (risk adjusted return): the ratio of Portolfio's Returns to Portfolio's Volatility (risk), annualized.\
The Sharpe Ratio gives market-participants the confidence to apply leverage.

## Output
```bash
Returns        0.445189
Volatility     0.197381
Sharpe Ratio   2.835657

SPY,0.15537764950322155
XLB,0.14840094378559168
XLE,0.11230647154471428
XLF,0.07320378035724731
XLI,0.00922948739999223
XLK,0.13076865641677185
XLP,0.13864787179631605
XLU,0.13783414102104255
XLV,0.06801761827474444
XLY,0.02621337990035807
```

### Code
Created 3 modules
- `config.py`: Define path as global variables
- `main.py`: Monte Carlo Simulation and calculating the max annualized sharpe-ratio and returns
- `data.py`: Extract the Adjusted-Closing Price for each SPDR Sector ETF

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

## Sources
https://www.sectorspdr.com/sectorspdr/
