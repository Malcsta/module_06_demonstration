"""
Description: Module 06 demonstration -
    Enumerations: An enumeration of the types 
    of bank accounts that PiXELL River supports.
Author: {student name}
Date: {current date}
Usage: To incorporate this enumeration into a class or 
program, import this enum using:
from account.account_type import AccountType 
"""

from enum import Enum

class AccountType(Enum):
    """
    An enumeration of the types of bank accounts supported
    by PiXELL River Financial.
    Values:
        SAVINGS: {description}
        CHEQUING
        MORTGAGE
        CREDIT
    """
    SAVINGS = 1
    CHEQUING = 2
    MORTGAGE = 3
    CREDIT = 4
    

