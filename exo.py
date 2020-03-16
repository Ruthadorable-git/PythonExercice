import math

class Employee(object):
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		
class SalaryManagement(object):
	def __init__(self):
		self.employees = []
		self.money = [200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
		self.total = [0 for i in range(len(self.money))]

	def addEmployee(self, name, salary):
		if len(self.employees) < 10:
			if salary > 5000 or salary <0:
                                return False 
			else:
				emp = Employee(name, salary)
				self.employees.append(emp)
				while salary != 0:
					for i, bill in enumerate(self.money):
						nb_bill = math.floor(salary / bill)
						if (nb_bill > 0):
							self.total[i] += nb_bill
							if (salary >= 1):
								salary = salary % bill
							else:
								salary = round(salary - bill * nb_bill,2) # corriger la précision
			return True
		return False

	def __repr__(self):
		s = "Aller chercher a la banque: \n"
		for i,c in enumerate(self.money):
			if c >= 5:
				s += str(self.total[i]) + " billet(s) de " + str(c) + "Eur" + "\n"
			else:
				s += str(self.total[i]) + " pièce(s) de " + str(c) + "Eur" + "\n"
		s += "\n Et les employés sont:\n"
		for emp in self.employees:
			s += "Nom: "+ emp.name + " Salaire: " + str(emp.salary) + "Eur\n"
			print(SalaryManagement())
		return s


	
if __name__ == '__main__':
	salMan = SalaryManagement()

	print("Ajouter Lionell 3578eur")
	if salMan.addEmployee("Lionell", 3578):
		print(salMan.total)


		
		
	print("Ajouter Charles 0.86eur")
	if salMan.addEmployee("Charles", 0.86):
		print(salMan.total)

	print("Ajouter Yves 6589.54eur")
	if salMan.addEmployee("Yves", 6589.54):
		print(salMan.total)
	else:
		print("Yves est trop blindé")

	print("Ajouter John -37.98eur")
	if salMan.addEmployee("Yves", -37.98):
		print(salMan.total)
	else:
		print("John est en dette")

	
	print(salMan)

	
