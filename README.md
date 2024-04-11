# Summary
Simple Bank App using Clean Architecture principles

# Setup
Clone the repo and do a simple `source venv/bin/activate` (on Mac)

# Demo
``` python
from bank import Bank

bank_app = Bank()

account = bank_app.register('jr', 'jr@email.com', '+639112223333')
# Account Number 881267668168 | Balance 0.00

bank_app.deposit(account, 500)
# Deposit 500 | Reference Code: 261711

bank_app.deposit(account, 200)
# Deposit 200 | Reference Code: 754603

bank_app.withdraw(account, 150)
# Withdraw 150 | Reference Code: 546789

bank_app.check_balance(account)
# 'Account Number 881267668168 | Balance 550.00'

bank_app.generate_statements(account)
# 'Deposit 500 | Reference Code: 261711\nDeposit 200 | Reference Code: 754603\nWithdraw 150 | Reference Code: 546789'

another_account = bank_app.register('not jr', 'not_jr@yopmail.com', '+63116669999')
bank_app.generate_statements(another_account)
# 'No Transactions for Account Number 772542680297'
```