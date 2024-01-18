class Bank:
   def __init__(self,balance = 0):
      self.balance = balance
      # self.__atm = atm
     
   def balance_check(self):
       print(f"ur balance is : {self.balance}") 
   def deposite(self,amount):
      if amount > 0:
         self.balance += amount

         print(f"Deposited ${amount}. New balance: ${self.balance}")
      else:
            print("Invalid deposit amount. Please enter a positive value.")
   def withdraw(self,amount):
       if 0 < amount <= self.balance:
           self.balance -= amount
           print(f"withdraw successfull . your balance is:{self.balance}")
       elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
       else:
            print("Insufficient funds for withdrawal.")
my_bank = Bank()
print(my_bank.balance_check())
print (my_bank.deposite(1500))
print (my_bank.withdraw(500))
