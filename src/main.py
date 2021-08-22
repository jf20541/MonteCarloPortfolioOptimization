import pandas as pd
import config
import numpy as np
from pprint import pprint


class PortfolioOptimization:
    def __init__(self, timeseries):
        self.timeseries = timeseries

    def get_log(self):
        """Returns: [float]:  Adjusted Closing Price Log-Returns"""
        return self.timeseries.apply(lambda x: np.log(x) - np.log(x.shift(1))).dropna()

    def weights(self):
        """Returns: [float]: Random balance weights for each asset"""
        random_weights = np.array(np.random.random(self.timeseries.shape[1]))
        rebalance_weights = random_weights / np.sum(random_weights)
        return rebalance_weights

    def sharpe_ratio(self, port_return, port_risk, risk_free=0.006):
        """Calculating Annualized Sharpe Ratio: (portfolio return - risk free rate) / porfolio volatility
        Args:
            port_return [float]: Portfolio's annusalized return
            port_risk [float]: Portfolio's annusalized risk (standard deviation)
            risk_free (float, optional): [1 year Bond]. Defaults to 0.006.
        Returns: [float]: [Annusalized Sharpe-Ratio]
        """
        port_return = np.sum((self.get_log().mean() * self.weights()) * 252) - 0.006
        port_risk = np.sqrt(
            np.dot(self.weights().T, np.dot(self.get_log().cov() * 252, self.weights()))
        )
        return port_return / port_risk

    def monte_carlo(self, n_iterations):
        """Monte Carlo simulating n_iterations
        Args:
            n_iterations [int]: Number of interations (Higher the number of iterations, higher will be the accuracy)
        """
        portfolio_weights = np.zeros((n_iterations, self.timeseries.shape[1]))
        returns, volatility, sharperatio = (
            np.zeros(n_iterations),
            np.zeros(n_iterations),
            np.zeros(n_iterations),
        )
        for iter in range(n_iterations):
            # randomizing weights, balancing them to 1
            weights = np.array(np.random.random(self.timeseries.shape[1]))
            weights = weights / np.sum(weights)

            # setting returns, volatility, and sharpe-ratio as numpy arrays
            returns[iter] = np.sum((self.get_log().mean() * weights) * 252) - 0.006
            volatility[iter] = np.sqrt(
                np.dot(weights.T, np.dot(self.get_log().cov() * 252, weights))
            )
            sharperatio[iter] = self.sharpe_ratio(
                returns[iter], volatility[iter], risk_free=0.006
            )

            portfolio_weights[iter, :] = weights

        # Build DataFrame, transpose, define columns, infer better datatype columns
        montecarlos_df = pd.DataFrame(
            data=[returns, volatility, sharperatio, portfolio_weights]
        ).T.infer_objects()
        montecarlos_df.columns = [
            "Returns",
            "Volatility",
            "Sharpe Ratio",
            "Portfolio Weights",
        ]

        # Find the Max Sharpe-Ratio and extract its respective weights for each Sector ETF
        max_sr = montecarlos_df.loc[montecarlos_df["Sharpe Ratio"].idxmax()]
        best_weights = montecarlos_df.loc[montecarlos_df["Sharpe Ratio"].idxmax()][
            "Portfolio Weights"
        ]
        sector_weights = pd.DataFrame(
            best_weights,
            ["SPY", "XLB", "XLE", "XLF", "XLI", "XLK", "XLP", "XLU", "XLV", "XLY"],
        )
        # Load the weights to the CSV file path
        sector_weights.to_csv(config.WEIGHTS_FILE)
        pprint(max_sr)
        pprint(sector_weights)


if __name__ == "__main__":
    df = pd.read_csv(config.TRAINING_FILE)
    df = df.set_index("Date")
    opt = PortfolioOptimization(df)
    pprint(opt.monte_carlo(1000))
