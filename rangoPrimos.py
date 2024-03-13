def es_primo(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
	
x= int(input("Rango hasta el que quieres conocer los números primos: "))

for i in range(2,x):
	if es_primo(i) == True:
		print(i)
