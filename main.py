#### Calculatrice Binaire :D ###
a=input("entrez le premier nombre binaire: ")
s=input("Entrer le signe de l'opération: ")
b=input("entre le second nombre binaire: ")
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
if "," in a or b:
     print("Cette calculatrice ne prend pas en charge les nombres décimal")
elif s == "+":
    e = f(a)+f(b)
    print(a,s,b,"=",bin(e)[2:])#pour afficher le résultat sans le 0b
elif s == "-":
    e= f(a)-f(b)
    print(a,s,b,"= -",bin(e)[3:])
elif s== "*":
    e= f(a)*f(b)
    print(a,s,b,"=",bin(e)[2:])
elif s== "/":
    e= f(a)/f(b)
    if type(e)!= int:
        print("Cette calculatrice ne prend pas en charge les nombres décimal")
    print(a,s,b,"=",bin(int(e))[2:])# pyhton ne prend pas les type float donc il faut préciser le int
elif s!="+" and s!="-" and s!="*" and s!="/":
    print("veuillez recommencer l'opération")


