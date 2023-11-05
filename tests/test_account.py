"""
Description: Module 06 demonstration -
    Unit Tests: Unit tests for the BankAccount class.
Author: {student name}
Date: {current date}
Usage: to execute tests:
    python -m unittest -v tests/account_tests.py
"""
import unittest

class AccountTests(unittest.TestCase):

    ## accessor tests needed:
    # 1. account_type accessor - returns account type attribute value (DEMONSTRATED)
    # 2. account_number accessor - returns account number attribute value
    # 3. balance accessor - returns balance attribute value

    ## __init__ tests needed:
    # 1. valid inputs  (DEMONSTRATED)
    # 2. invalid account type (DEMONSTRATED)
    # 3. invalid account number (non-numeric)
    # 4. invalid account number (negative)
    # 4. invalid balance (non-numeric)


    ## mutator tests needed:
    # 1. account_type mutator - valid input (DEMONSTRATED)
    # 2. account_type mutator - invalid input (DEMONSTRATED)
    # 3. account_number mutator - valid input
    # 4. account_number mutator - non-numeric
    # 5. account_number mutator - negative
    # 6. balance mutator - valid input
    # 7. balance mutator - non-numeric

    ## __repr__ tests:
    #1. ensure expected representation is returned. (DEMONSTRATED)

    ## __str__ tests:
    # 1. ensure expected string representation is returned. (DEMONSTRATED)

    ## update_balance tests:
    #1. valid deposit
    #2. valid withdraw
    #3. non-numeric amount
    #4. insufficient funds  (DEMONSTRATED)
