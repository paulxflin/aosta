# Trading-AI

Trading-AI is a Python library for automated trading.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

Create your own config.py.

```python
# config.py

# Login
email = 'sample@gmail.com'
password = 'your_password'

# Parameters
stock = 'apple'
delta = 0
status = 0
start_capital = 100
goal = 10000
spread = 0.001
profit_margin = 0.005

# Market Information
high, low = 1.3, 1.1
daily = (high, low, (high+low)/2)
weekly = (high, low, (high+low)/2)

```

Start the advisor in shell.

```python
# Python REPL
from advisor import Advisor

# Start the Advisor
Advisor()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)