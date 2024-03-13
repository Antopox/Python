n= int(input("Número de plantas del árbol: "))

for i in range(n):
	print((n-i)*" ",i*"*","*",i*"*",sep="")

for x in range(7):
	print((n-1)*" ","*")
