import os
from argparse import ArgumentParser

from finrl import config

from finrl.config_tickers import DOW_30_TICKER
from finrl.config import (
    DATA_SAVE_DIR,
    TRAINED_MODEL_DIR,
    TENSORBOARD_LOG_DIR,
    RESULTS_DIR,
    TECHNICAL_INDICATORS_LIST,
    TRAIN_START_DATE,
    TRAIN_END_DATE,
    ERL_PARAMS,
    RLlib_PARAMS,
    SAC_PARAMS,
)


# construct environment
from finrl.finrl_meta.env_stock_trading.env_stocktrading_np import StockTradingEnv

def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--mode",
        dest="mode",
        help="start mode, train, download_data" " backtest",
        metavar="MODE",
        default="train",
    )
    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()
    if not os.path.exists("./" + DATA_SAVE_DIR):
        os.makedirs("./" + DATA_SAVE_DIR)
    if not os.path.exists("./" + TRAINED_MODEL_DIR):
        os.makedirs("./" + TRAINED_MODEL_DIR)
    if not os.path.exists("./" + TENSORBOARD_LOG_DIR):
        os.makedirs("./" + TENSORBOARD_LOG_DIR)
    if not os.path.exists("./" + RESULTS_DIR):
        os.makedirs("./" + RESULTS_DIR)

    if options.mode == "train":
        from finrl import train

        env = StockTradingEnv

        # demo for elegantrl
        kwargs = {}  # in current finrl_meta, with respect yahoofinance, kwargs is {}. For other data sources, such as joinquant, kwargs is not empty
        train(
            start_date=TRAIN_START_DATE,
            end_date=TRAIN_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=TECHNICAL_INDICATORS_LIST,
            drl_lib="elegantrl",
            env=env,
            model_name="ppo",
            cwd="./test_ppo",
            erl_params=ERL_PARAMS,
            break_step=1e5,
            kwargs=kwargs,
        )


if __name__ == "__main__":
    main()
