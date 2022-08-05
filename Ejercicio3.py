#Entradas
RC = int (input())
print ("Ingrese numero de respuestas incorrectas")
RI = int(input())
print ("INgrese numero de respuestas en blanco")
RB = int(input())

#Proceso
PCR=RC*3 
PRI=RI*-1
PRB=RB*0
PF=PCR + PRI +PRB

print (PF)