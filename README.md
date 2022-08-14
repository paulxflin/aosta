# Agnostic Open Source Trading Advisor (AOSTA)

Open Source Trading Advisor created for Educational Purposes and Permissive Personal Use.

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

### You May:
- Read, write, modify, extend, share, template, and personal use (including for profit)

### You May NOT:
- Use for Private Business

### Ownership:
- [Paul Lin](https://www.github.com/paulxflin)
- [Moderne](https://www.linkedin.com/company/moderne-soc/)

### Legal Statement
You may use AOSTA exclusively for personal use, in which it's fully permissive. However, you may not use AOSTA for profit within a private business environment. All intellectual rights for AOSTA belongs jointly to [Paul Lin](https://www.github.com/paulxflin) and [The School of Moderne Society](https://www.linkedin.com/company/moderne-soc/), incorporated through Stripe in Delaware, on July 2022. 
