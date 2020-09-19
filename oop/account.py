import datetime
import pytz
import time

class Account:
    """ simple account with class
    account
    """
    @staticmethod
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return {pytz.utc.localize(utc_time),2}
    # _ -> private method

    @staticmethod
    def current_time():
        utc_time=datetime.datetime.utcnow()
        return {pytz.utc.localize(utc_time),2}


    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def show_balance(self):
        print("Balance {}".format(self.__balance))

if __name__=='__main__':
    a=Account("a",0)
    a.show_balance()
    a.deposit(100)
    a.show_balance()
    # print(datetime.datetime.utcnow())
    # print(list(Account.current_time())[1])
    # time.sleep(1)
    # print(Account.current_time())
    print(a.__dict__)
    a.deposit(100)
    print(a.__dict__)
    print(a._Account__balance)
    # prevents accidental shadowing
    # when creating some attributes
