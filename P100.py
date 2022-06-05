class Atm(object):
  """
    blueprint for car
  """

  def __init__(self, card_number, pin_number):
    self.card_number = card_number
    self.pin_number = pin_number

  def withdraw(self):
    print("withdrawing...")

  def balanceEnqiry(self):
    print("enqiring...")

  def deposit(self):
    print("depositing")


person1 = Atm(406475634534, 4534)

person1.withdraw()
person1.deposit()
person1.balanceEnqiry()