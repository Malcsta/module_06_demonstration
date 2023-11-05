"""
Description: Module 06 demonstration -
    Class: A class that maintains bank accounts 
    at PiXELL River.
Author: {student name}
Date: {current date}
Usage: To incorporate this class into a class or 
program, import this using:
from account.account_type import Account 
"""

## CLASS
# given docstring for class
"""
A class that maintains bank account data.

Attributes:
    _account_type (AccountType): The type of bank account.
    _account_number (int): Account number of the bank account.
    _balance (float): Balance of the bank account.

Methods (instance methods):
    update_balance(): Modifies the balance of the bank account.
"""

## __INIT__
# given docstring for __init__
"""
Initialize a new account object with an account type,
account number and balance.
Args:
    account_type(AccountType): The account type for the account.
    account_number(int): The account number for the account.
    balance (float): The balance of the account.
Returns:
    None
Raises:
    ValueError: When the account type is invalid.
    ValueError: When the account number is non-numeric.
    ValueError: When the account number is negative.
    ValueError: When the balance is non-numeric.
"""

## ACCESSORS

## MUTATORS
# given docstring for account type mutator:
"""
Sets the account type of the Account.
Args:
    value (AccountType): The type of account.
Raises:
    ValueError: When the value provided is 
    not a valid AccountType.
"""

# given docstring for acount number mutator:
"""
Sets the account number of the Account.
Args:
    value (int): The account number.
Raises:
    ValueError: When the value provided not numeric.
    ValueError: When the value provided is negative.
"""

# given docstring for balance mutator:
"""
Sets the balance of the Account.
Args:
    value (float): The account balance.
Raises:
    ValueError: When the value provided not numeric.
"""


## __REPR__
# given docstring for __repr__
"""
Provides a representation of an Account object.
Returns:
    str: A representation of a bank account.
        format: account_type | account_number | balance
        example: [AccountType.MORTGAGE | 1234567 | -493912.53]
"""

## __STR__
# given docstring for __str__
"""
Returns a string representation of the class.
Returns:
    str:  A string representation of a bank account.
        format:  Type: AccountType
                Account Number: account number
                Balance: $balance
        example:
                Type: Mortgage
                Account Number: 1234567
                Balance: $-493,912.53    
"""

## UPDATE_BALANCE
# given docstring for update_balance()
"""
Update the balance of the account.  All deposits (+) are 
permitted.  Withdraws (-) are only permitted if sufficient funds.

Args:
    amount(float): amount of transaction.  Positive values 
    are deposited, negative values are withdrawn.

Returns:
    None
Raises:
    ValueError: When the amount is non-numeric.
    ValueError: When there are insufficient funds.
"""