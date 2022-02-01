class Atm():
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print("you have a balance of $50.00")

    def cashwithdrawal(self, amount):
        new_amount=50-amount
        print("you have withdrawn: " + str(amount) + "Your new balance is: " + str(new_amount))
    
def bank():
        name=input("What is your name?")
        print("Hello, "+name)
        cardnumber= input("insert card number here: ")
        pin=input("enter your PIN: ")
        new_user=Atm(cardnumber, pin)

        print("what do you want to do?")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        activity=int(input("Enter your choice: "))

        if (activity == 1):
            user.balanceinquiry()
        elif(activity== 2):
            amount= int(input("Enter the amount"))
            new_user.cashwithdrawal(amount)
        else:
            print("Invalid choice")
if __name__  == "__bank__":
    bank()
    






    

