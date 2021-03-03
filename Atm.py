class Atm (object):
    def __init__ (self,payment,color,company,keypad):
        self.color=color
        self.payment=payment
        self.company=company
        self.keypad=keypad

    def pay (self):
        print('payed!')

    def CashWithdrawl (self):
        print('With drawl money!') 

    def acces_bank (self):
        print('here is your bank account!') 

Debit=Atm( 500,'red','debit',200)  

print(Debit.pay())
print(Debit.CashWithdrawl())
print(Debit.acces_bank())