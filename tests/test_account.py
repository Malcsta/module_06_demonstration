"""
Description: Module 06 demonstration -
    Unit Tests: Unit tests for the BankAccount class.
Author: {student name}
Date: {current date}
Usage: to execute tests:
    python -m unittest -v tests/account_tests.py
"""
import unittest
from account.account import Account
from account.account_type import AccountType 


class AccountTests(unittest.TestCase):


    ## accessor tests needed:
    # 1. account_type accessor - returns account type attribute value (DEMONSTRATED)
    # 2. account_number accessor - returns account number attribute value
    # 3. balance accessor - returns balance attribute value

    def test_account_type_accessor(self):

        #Arrange
        account = Account(AccountType.SAVINGS, 99999, 559.95)
        expected = AccountType.SAVINGS
        
        #Act
        actual = account.account_type # dont need parenthesis with accessor because it's been decorated

        #Assert
        self.assertEqual(expected, actual)


    ## __init__ tests needed:
    # 1. valid inputs  (DEMONSTRATED)
    # 2. invalid account type (DEMONSTRATED)
    # 3. invalid account number (non-numeric)
    # 4. invalid account number (negative)
    # 5. invalid balance (non-numeric)

    def test_init_valid(self):

        #Arrange
        account_type = AccountType.MORTGAGE
        account_number = 1234567
        balance = 100.50

        account = Account(account_type, account_number, balance)

        #Act and assert
        self.assertEqual(account_type, account.account_type)
        self.assertEqual(account_number, account.account_number)
        self.assertEqual(balance, account.balance)

    def test_init_invalid_account_type(self):

        #Arrange
        account_type = "INVALID"
        account_number = 1234567
        balance = 100.50

        #Act and asssert
        with self.assertRaises(ValueError) as context:
            Account(account_type, account_number, balance)

        self.assertEqual(str(context.exception), "Invalid account type.")


    ## mutator tests needed:
    # 1. account_type mutator - valid input (DEMONSTRATED)
    # 2. account_type mutator - invalid input (DEMONSTRATED)
    # 3. account_number mutator - valid input
    # 4. account_number mutator - non-numeric
    # 5. account_number mutator - negative
    # 6. balance mutator - valid input
    # 7. balance mutator - non-numeric
    
    def test_account_type_mutator_valid(self):

        #Arrange
        account = Account(AccountType.CREDIT, 1234567, 100.59)
        expected = AccountType.CHEQUING

        #Act
        account.account_type = AccountType.CHEQUING

        #Assert
        self.assertEqual(expected, account.account_type)
    

    def test_account_type_mutator_invalid(self):

        #Arrange
        account = Account(AccountType.MORTGAGE, 1234567, 5003.20)
        expected = "Invalid account type."

        #Act and assert
        with self.assertRaises(ValueError) as context:
            account.account_type = 'INVALID'

        self.assertEqual(str(context.exception), expected)


    ## __repr__ tests:
    #1. ensure expected representation is returned. (DEMONSTRATED)

    def test_repr_valid(self):

        #Arrange
        account = Account(AccountType.MORTGAGE, 1234567, 123.4567)
        expected = "AccountType.MORTGAGE | 1234567 | 123.4567"

        #Act
        actual = repr(account)

        #Assert
        self.assertEqual(expected, actual)



    ## __str__ tests:
    # 1. ensure expected string representation is returned. (DEMONSTRATED)

    def test_str_valid(self):

        #Arrange
        account = Account(AccountType.MORTGAGE, 1234567, -493912.53)
        expected = ('Type: Mortgage \n'
                    'Account Number: 1234567 \n'
                    'Balance: $-493,912.53'
        )

        actual = str(account)

        self.assertEqual(expected, actual)

    ## update_balance tests:
    #1. valid deposit
    #2. valid withdraw
    #3. non-numeric amount
    #4. insufficient funds  (DEMONSTRATED)

    def test_update_balance_insufficient_funds(self):

        #Arrange
        account = Account(AccountType.SAVINGS, 1234567, 5000)
        expected = 'Insufficient funds!'

        #Act
        with self.assertRaises(ValueError) as context:
            account.update_balance(-5001)

        #Assert
        self.assertEquals(str(context.exception), expected)