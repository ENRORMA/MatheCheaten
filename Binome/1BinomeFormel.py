#!/bin/python3
import random
print("Die erste binomische formel ist:")
print("  (a + b)\u00b2")
print(f"= a\u00b2 + 2ab + b\u00b2\n\n")

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
		print(f"({a}x + {b})\u00b2")
		print(f"{a}x\u00b2 + {2 * (a * b)}x + {b}\u00b2")
		print(f"{a}x\u00b2 + {2 * (a * b)}x + {b*b}")
	else:
		print(f"({a} + {b}x)\u00b2")
		print(f"{a}\u00b2 + {2 * (a * b)}x + {b}x\u00b2")
		print(f"{a * a} + {2 * (a * b)}x + {b}x\u00b2")
	print("-------------------------------------------------------")