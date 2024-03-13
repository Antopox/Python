from itertools import count


def valEmail(aux):
    if aux.count("@") == 1 and aux.count(".") == 1 and aux.count(" ") == 0:
        return 1
    else:
        return 0
        
      
EmailValid = []
EmailInvalid = []
cont = True

while cont:
    aux = input("Introduce un email o salir: ")
    if aux == "salir":
        cont = False
    else:
        if valEmail(aux) == 1:
            EmailValid.append(aux)
        else:
            EmailInvalid.append(aux)
            

print("Emails validos: ")

for i in EmailValid:
    print(i)
    
print("Emails invalidos: ")

for i in EmailInvalid:
    print(i)
    