from app.calculations import add,subtract,multiply,divide,BankAccount
import pytest


@pytest.fixture() # To set a default value for the fixture
def zero_bank_account():
     return BankAccount()

@pytest.fixture() # To set a default value for the fixture
def bank_account():
     return BankAccount(50)



@pytest.mark.parametrize("num1,num2,expected",[(1,2,3),(2,4,6)]) # Takes function parameter to get chcked.
def test_add(num1,num2,expected):

     sum= add(num1,num2)
     assert sum==expected



@pytest.mark.parametrize("num1,num2,expected",[(2,1,1),(4,2,2)])
def test_subtract(num1,num2,expected):

     sum= subtract(num1,num2)
     assert sum==expected


def test_multiply():

     sum= multiply(5,3)
     assert sum==15


def test_divide():

     sum= divide(6,3)
     assert sum==2






def test_bankaccount(zero_bank_account):
   
     assert zero_bank_account.balance==0





def test_bank_diposit(bank_account): # Every bank_account class instance is different.
     bank_account.diposit(50)
     assert bank_account.balance==100




def test_bank_withdrow(bank_account): # Every bank_account class instance is different.
     bank_account.withdrow(20)
     print(bank_account.balance)
     assert bank_account.balance==30




def test_collect_interest(bank_account): # Every bank_account class instance is different.
     bank_account.collect_interest()
     assert round(bank_account.balance,6)==55







def test_bank_transaction(zero_bank_account): # Every bank_account class instance is different.
                                              # We can use different methods of a single instance.
     zero_bank_account.diposit(200)
     zero_bank_account.withdrow(50)
     assert zero_bank_account.balance==150


@pytest.mark.parametrize("diposit,withdrow,expected",[(200,100,100),(500,300,200)])


def test_bank_transaction_using_fixture(zero_bank_account,diposit,withdrow,expected): # Every bank_account class instance is different.
                                              # We can use different methods of a single instance.
     zero_bank_account.diposit(diposit)
     zero_bank_account.withdrow(withdrow)
     assert zero_bank_account.balance==expected






# How do we tell pytest that we expect an error in a test?

def test_bank_transaction_error(bank_account): # Every bank_account class instance is different.
     
     with pytest.raises(Exception): # We are telling pytest we expect an exception error.
          # Our Exception should be specific all the time.Means what kind of exception we raised
          # this exception must be the same.
        bank_account.withdrow(100) # Raises an excepion and passes

#(pytest -v -s) to see test result in details









