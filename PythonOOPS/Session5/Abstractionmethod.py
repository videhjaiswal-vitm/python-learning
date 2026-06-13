from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        """All payment methods must implement this method"""
    pass


# Concrete subclass 1
class CreditCardPayment(Payment):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount} for {self.card_holder}")
        # (Implementation details hidden)
        print("✅ Payment successful using Credit Card!")    

# Concrete subclass 2
class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email
 
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount} for {self.email}")
        # (Implementation details hidden)
        print("✅ Payment successful using PayPal!")

# Function that uses abstraction
def make_payment(payment_method: Payment, amount):
    """This function doesn't care *how* the payment works — only that it can 'pay'."""
    payment_method.pay(amount)
 
 
# ✅ Using the system
credit = CreditCardPayment("1234-5678-9999-0000", "Alice")
paypal = PayPalPayment("alice@example.com")
 
make_payment(credit, 1500)
print()
make_payment(paypal, 300)

'''
Concept Description
Abstraction
The class Payment defines the general idea of a payment (via pay()), but not how it works.
 
Implementation Hiding
The details of how Credit Card or PayPal payments are processed are hidden inside subclasses.

Flexibility
You can add new payment methods (e.g., CryptoPayment, BankTransferPayment) without changing other code.
 
Polymorphism
The function make_payment() works with any subclass of Payment.

#Abstraction helps you design clean, extensible, and flexible systems — focusing on what objects do, not how they do it.
 
Why do we need the Payment class?
I can just add a pay() method directly in CreditCardPayment or PayPalPayment.”
 
✅ You’re absolutely right — if your program only ever needs one payment method,
you can skip the abstract base class and just use your CreditCardPayment class directly.
==========================
But Here’s the Key Reason for the Payment Abstract Class
 
The abstract class (Payment) defines a common interface that all payment methods must follow.
It enforces a contract — saying:
Any class that represents a payment must have a pay(amount) method.
 
That means you can write code that uses Payment objects without caring which specific subclass is being used.
This makes your program flexible, extendable, and easier to maintain.
'''