class SavingAccount():
    pass

class CheckingAccount():
    pass

class Stock():
    pass

class Bond():
    pass

class Security(Stock, Bond):
    pass

class BankAccount(SavingAccount, CheckingAccount):
    pass

class RealEstate():
    pass

class InterestBearingItem(BankAccount, Security):
    pass

class Assest(BankAccount, RealEstate, Security):
    pass

class InsuableItem(BankAccount, RealEstate):
    pass

