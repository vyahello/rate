# Exchange rate

## Basic exchange rates for UAH currency
- `rate.py` tool allows to get exchange rate for `UAH` currency on particular date.
```
~ python rate.py --help
usage: rate.py [-h] --currency CURRENCY [--date DATE]

Allow to get exchange rate of specific currency to `uah`.

optional arguments:
  -h, --help            show this help message and exit
  --currency CURRENCY, -c CURRENCY
                        Currency to interpret into `uah` exchange rate
                        comparision. For instance `usd` represents dollar
                        currency. (default: None)
  --date DATE, -d DATE  Date should be in YYYY-MM-DD format. Default is today
                        date. (default: 2018-04-15)
```
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.