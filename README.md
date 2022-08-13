# Agnostic Open Source Trading Advisor (AOSTA)

Open Source Trading Advisor created by Paul Lin for educational purposes.

## Installation

Issue in bash/powershell/terminal:

```bash
git clone [url]
cd aosta
```

## Usage

Create your own config.py:

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

Please make sure to add/update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/#)

License TLDR: You are allowed to read, write, and share, but not permitted to make a copy for private business customers, i.e. the products you create must be open to public. You are allowed to fork, modify, and build your own automated trader on top of AOSTA. 
