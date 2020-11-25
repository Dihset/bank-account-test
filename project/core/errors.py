from tortoise.exceptions import DoesNotExist


class AccountException(Exception):
    '''Base Account exception'''
    message = 'some message'
    status_code = 400


class AccountDoesNotExist(AccountException, DoesNotExist):
    '''
    The AccountDoesNotExist exception is raised when expecting data, such as a ``Account.get()`` operation.
    '''
    message = 'Account not found'
    status_code = 404


class AccountNegativeBalance(AccountException):
    '''
    The balance cannot be negative
    '''
    message = 'The balance cannot be negative'
    status_code = 400

