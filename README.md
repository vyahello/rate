[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# UAH exchange rate
> Obtains exchange rate for `uah` currency depending on a particular type of currency on a specific date.

## Tools

- python 3.6, 3.7, 3.8
- [requests](https://requests.readthedocs.io/en/master) library
- [black](https://black.readthedocs.io/en/stable/) code formatter

### Usage

```bash
python rate.py --currency pln
2018-06-11 12:08:44     Exchange rate for UAH/PLN is 7.178 on 11.06.2018
python rate.py --currency usd
2018-06-11 12:08:50     Exchange rate for UAH/USD is 26.136 on 11.06.2018
python rate.py --currency usd --date 2008-11-06
2018-06-11 12:09:19     Exchange rate for UAH/USD is 5.822 on 06.11.2008
python rate.py --currency pln --date 2008-11-06
2018-06-11 12:09:44     Exchange rate for UAH/PLN is 2.130 on 06.11.2008
```

### Quick start
```bash
git clone git@github.com:vyahello/terminal-uah-rate.git
pip install -r requirements.txt
python rate.py --help
```

### Testing
Run `pytest -v` from shell in the root directory of the repository.

### Contributing
1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. Create your feature branch (`git checkout -b feature/fooBar`)
5. Commit your changes (`git commit -am 'Add some fooBar'`)
6. Push to the branch (`git push origin feature/fooBar`)
7. Create a new Pull Request
