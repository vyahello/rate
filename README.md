# UAH exchange rate
Gets exchange rate for uah currency depending on a particular type of currency on a specific date.

## Exchange rates for uah currency
- `rate.py` tool allows to get exchange rate for `uah` currency on particular date.

## Demo
```bash
~/rate python rate.py --currency eur
2018-06-11 12:08:24     Exchange rate for UAH/EUR is 30.720 on 11.06.2018
~/rate python rate.py --currency pln
2018-06-11 12:08:44     Exchange rate for UAH/PLN is 7.178 on 11.06.2018
~/rate python rate.py --currency usd
2018-06-11 12:08:50     Exchange rate for UAH/USD is 26.136 on 11.06.2018
~/rate python rate.py --currency usd --date 2008-11-06
2018-06-11 12:09:19     Exchange rate for UAH/USD is 5.822 on 06.11.2008
~/rate python rate.py --currency eur --date 2008-11-06
2018-06-11 12:09:39     Exchange rate for UAH/EUR is 7.493 on 06.11.2008
~/rate python rate.py --currency pln --date 2008-11-06
2018-06-11 12:09:44     Exchange rate for UAH/PLN is 2.130 on 06.11.2008
~/rate python rate.py --currency usd --date 2008-11-06
2018-06-11 12:09:51     Exchange rate for UAH/USD is 5.822 on 06.11.2008
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
