# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:22:24 2020

@author: carlos
"""
# Ejercicios con Brenda Scarleth
# =============================================================================
# Problema 0
# Dado un arreglo de longitud 1 o mas regresa la dif entree el num mas grande y el mas chico del arreglo
# =============================================================================

def diffmaxmin(arreglo):
    return max(arreglo)-min(arreglo)
print(diffmaxmin([1,2,3,4]))
#if __name__ = "__main__": 
"""
try:
    x = int(input("Cuantos numeros tendra el arreglo?\t"))
except:
    print("ERROR")
y=[]
for i in range(x):
    try:
        y.append(int(input("Cual es el numero",i+1,"?\t")))
    except:
        print("ERROR")
print(diffmaxmin(y))
#La manera que querian que lo hiciera...
def diffmaxmin1(arreglo):
    maxx=0
    minn=0
    for i in range(len(arreglo)):
#el proposito era usar for y ciclos y fallamos :c
"""        
# =============================================================================
# Problema 1
# arreglo de ints long min de 1 devolde la cantidad de numeros exactamente la misma cantidad e veces que su valor
# =============================================================================
exam=[1,2,3,43,5,2]
exam1=[]
exam2=[3,3,3]

def numexac(arreglo):
    dicc={}
    s=0
    for i in arreglo: 
        s = dicc.get(i,0)
        dicc[i] = s + 1
    finarreglo=[]
    for i in list(dicc):
        if i==dicc[i]:
            finarreglo.append(i)
    return len(finarreglo),finarreglo

def numexac1(arreglo):
    summ=0
    for i in range(len(set(arreglo))):
        #thenum
        if list(set(arreglo))[i]==arreglo.count(list(set(arreglo))[i]):
            summ+=1
    return summ


# =============================================================================
# # Problema 2
# # dados 2 arreglos n1 y n2 de la misma len para cada elemen de n1  considera que 
# # tiene el mismo index, regresa la cantidad de veces que 2 elementos difieren por mas de 2 o menos
# # PERO que no sean iguales
# 
# =============================================================================
exam3=[2,3,4]
def matchUpeame(n1,n2):
    summ=0
    for i in range(len(n1)):
        if abs(n1[i]-n2[i])<=2 and abs(n1[i]-n2[i]) !=0:
            summ+=1
    return summ

# =============================================================================
# Problema 3
# ... Fizzbuzz modificado
# =============================================================================

def threefive(start,end):
    result=[]
    for i in range(start,end):
        if i%3==0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def threefive1(start,end):          #Sin append y sin elif
    result=list(range(start,end))
    for i in range(len(result)):
        result[i]='' 
    for i in range(start,end):
        if i%5==0 or i%3==0:
            if i%3==0:
                result[i-start]=result[i-start]+"Fizz"
            result[i-start]=result[i-start]+"Buzz"
        else:
            result[i-start]=str(i)
    return result

"""
for i in range(len(ejem)):
    if arr[i]<arr[i+1]:
"""

def haber(arr):
    #ejem lista
    summ=0
    ejem=list(range(1,len(arr)+1))
    temp=True
    for i in range(len(arr)):
        if arr[i]-ejem[i]>2:
            print("Too chaotic")
            temp=False
            break
        elif arr[i]-ejem[i]<=2 and arr[i]-ejem[i]>0:
            if arr[i]-ejem[i]==2 and arr[i+1]>arr[i+2]:     #esto esta mal pero funciona
                summ+=1                                     #srry  
            summ+=arr[i]-ejem[i]
    if temp:
        return None
    else:
        return summ
#imple/dev test deploy stage
x=[int(i)for i in input("Introduce la lista, separada por espacios...\t").split()]
print("",haber(x))
