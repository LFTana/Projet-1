#### Calculatrice Binaire uniquement pour les entiers positifs avec comme opération les addition et multiplication :D ###
a=input("entrez le premier nombre binaire entier et positif: ")
s=input("Entrer le signe de l'opération (soit + soit *): ")
b=input("entre le second nombre binaire entier et positif: ")
e=0
def f(x):      #c'est la fonction pour convertir decimale binaire :)#
    xdec=int(0)
    r=int(len(x))-1 #c'est le rang pour l'opération
    for str in x:
        if str=="1":
            xdec=xdec+(1*2**r)
            r=r-1
        else:
            r=r-1
    return(xdec)
if s=="+" or s=="*":
    if "+" in s:
        e=f(a)+f(b)
    if "*" in s:
        e=f(a)*f(b)
    print(a,s,b,"=",bin(e)[2:])
else:
    print("veuillez recommencer, l'opération n'a pas été reconue")
