#!/bin/python3
import random
print("Die dritte binomische formel ist:")
print("  (a + b) * (a - b)")
print(f"= a\u00b2 - b\u00b2\n\n")

Counter = int(input("Wie Viele: "))

while Counter != 0:
	Counter += -1
	a = random.randrange(2,20)
	b = random.randrange(2,20)
	foo = random.randrange(0,2)
	if foo == 0:
		FirstIsX = True
	else:
		FirstIsX = False

	if FirstIsX == True:
		print(f"({a}x + {b}) * ({a}x - {b})")
		#print(f"{a}\u00b2 - {a}*{b} + {a}*{b} - {b}\u00b2")
		print(f"{a*a}x\u00b2 - {b*b}")
	else:
		print(f"({a} + {b}x) * ({a} - {b}x)")
		print(f"{a*a} - {b*b}x\u00b2")
	print("--------------------")
