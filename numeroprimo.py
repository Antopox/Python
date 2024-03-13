def es_primo(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
	
x= int(input("Que número quieres saber si es primo: "))

print(es_primo(x))
