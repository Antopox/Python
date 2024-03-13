primos= []

def es_primo(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
	
n= int(input("Número para factorizar :"))

for i in range(2,n):
	if es_primo(i) == True:
		primos.append(i)

for i in primos:
	while n%i==0:
		print(i)
		n=n/i

