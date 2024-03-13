sumandos=[]
ans=0
q=input("Continue or quit?: ")

while q!="quit":
	sumandos.append(float(input("-")))
	sumandos.append(float(input("-")))
	sumandos.append(float(input("-")))
	for i in sumandos:
		if i==ans:
			ans=ans+ans   
		ans=ans+i
	print(ans)
	q=input("Continue or quit?: ")
