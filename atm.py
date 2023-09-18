class ATM:
    def __init__(self):
        self.__balance = 0
        self.__pin = ''
        #self.menu()
        
        
    def get_pin(self):
        return self.__pin
    

    def change_pin(self, newPin):
        if type(newPin) == str:
            self.__pin = newPin
            print('pin changed')
        else:
            print('not allowed')
        
    def menu(self):
        user_input = int(input('''
                           hELLO! hOW WOULD U LIKE TO PROCEED!
                           1- enter 1 to create pin  
                           2- enter 2 to withdraw  
                           3- enter 3 to deposit  
                           4- enter 4 to check balance  
                           5- enter 5 to change pin  
                           6 enter 6 to exit  
                           '''))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.withdraw()
        elif user_input == 3:
            self.deposit()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            self.change_pin()
        else:
            print('Thank You, Bye!\n')
            
    
    def create_pin(self):
        self.__pin = input('enter your pin ')
        print('your pin has been set\n')
        
        self.next_step()
        
        
    def withdraw(self):
        temp = input('please enter your pin ')
        if temp == self.__pin:
            amount = int(input('please enter the amount you want to withdraw '))
            if amount <= self.__balance:
                self.__balance -= amount
                print('you have successfully withdrawn your money\n')
            else:
                print('you do not have enough balance\n')
        else:
            print('Invalid Pin\n')
            self.next_step()
            
        
            
            
    def deposit(self):
        temp = input('please enter your pin ')
        if temp == self.__pin:
            amount = int(input('please enter the amount u wish to deposit '))
            self.__balance += amount
            print('you have successfully deposited money to your account\n')
        else:
            print('invalid pin\n')
        self.next_step()
        
            
    def check_balance(self):
        temp = input('please enter your pin ')
        if temp == self.__pin:
            print('your account balance is: ' + str(self.__balance))
        else:
            print('invallid pin\n')
        self.next_step()
  
            
            
    def next_step(self):
        more = input('do u want to continue, Y/N: ')
        if more == 'y':
            self.menu()
        else:
            print('Thank you for using our service ')
        
            
def main():
    sbi = ATM()
    sbi.menu()
    # Displaying the value returned by get_pin method
    pin_value = sbi.get_pin()
    print("Current PIN:", pin_value)

    # Setting a new PIN and displaying success or failure
    new_set_pin = input('enter the new pin that you wish to set: ')
    sbi.change_pin(new_set_pin)
    new_pin = sbi.get_pin()
    print("Current PIN:", new_pin)

    if new_pin == new_set_pin:
        print("PIN set successfully:", new_pin)
    else:
        print("PIN set failed")

    sbi.menu()

    
if __name__ == '__main__':
    main()
        