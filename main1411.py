class Employee:
  def __init__(self, first, last, pay, bonus=0):
      self.first = first
      self.last = last
      self.email = f'{first}.{last}@email.com'
      self.pay = pay
      self.bonus = bonus

  def calculate_bonus(self, bonus_rate):
      return self.pay * bonus_rate

  def fullname(self):
      return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ahson', 'Razeen', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


bonus_rate_emp_1 = 0.05  
bonus_rate_emp_2 = 0.1   

bonus_emp_1 = emp_1.calculate_bonus(bonus_rate_emp_1)
bonus_emp_2 = emp_2.calculate_bonus(bonus_rate_emp_2)

print(f"Bonus for {emp_1.fullname()}: ${bonus_emp_1:.2f}")
print(f"Bonus for {emp_2.fullname()}: ${bonus_emp_2:.2f}")