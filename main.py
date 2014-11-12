#### Calculatrice Binaire :D ###
a=input("entrez le premier nombre binaire")
s=input("Entrer le signe de l'opération")
b=input("entre le second nombre binaire")
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
if s == "+":
    e = f(a)+f(b)
if s == "-":
    e= f(a)-f(b)
if s== "*":
    e= f(a)*f(b)
if s== "/":
    e= f(a)/f(b)
else :
    print("veuillez recommencer l'opération")
print(a,s,b,"=",bin(e)) #g la fonction "bin" sur python converti les nombres décimal en binaire après l'opération

