




def add(num1:int,num2:int):
    return num1+num2






def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):

    return num1 / num2




class BankAccount():
  def __init__(self, starting_balance=0):
    self.balance=starting_balance

  def diposit(self,amount):
      self.balance+=amount

  def withdrow(self,amount):
      if self.balance<amount:
          raise Exception("insufficient balance")

          
      self.balance-=amount
      
  def collect_interest(self):
      self.balance*=1.1
      






