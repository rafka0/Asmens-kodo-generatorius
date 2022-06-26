# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:56:26 2022

@author: Vartotojas
"""
print("Asmens kodo generatorius.")
print("Visi kodai yra atsitiktiniai, programa skirta tik generavimui, be jokio piktybiško panaudojimo.")
print("https://github.com/rafka0")
print("\n")

while 1>0:
    a1=input("Lytis (V/M):")
    a1=a1.upper()
    b1=input("YYYY:")
    b=b1[-2:]
    b2=int(b1[0])
    
    if b2==1:
        if a1=="V":
            a=3
        if a1=="M":
            a=4
            
    if b2==2:
        if a1=="V":
            a=5
        if a1=="M":
            a=6
            
    
    c=input("MM:")
    
        
    d=input("DD:")
    pradzia=str(a)+str(b)+str(c)+str(d)
    print("Asmens kodo pradžia: ",pradzia)
    
    galas=[]
    beveik=[]
    visi=[]
    for i in range(0,1000):
        x=(f"{i:03}")
        x=str(x)
        x=galas.append(x)
        
    for y in range(len(galas)):
        priesgal=pradzia+galas[y]
        presgal=beveik.append(priesgal)
    
    for g in range(len(beveik)):
        kodas1=beveik[g]
        a=kodas1[0]
        a=int(a)
        b=kodas1[1]
        b=int(b)
        c=kodas1[2]
        c=int(c)
        d=kodas1[3]
        d=int(d)
        e=kodas1[4]
        e=int(e)
        f=kodas1[5]
        f=int(f)
        g=kodas1[6]
        g=int(g)
        h=kodas1[7]
        h=int(h)
        i=kodas1[8]
        i=int(i)
        j=kodas1[9]
        j=int(j)
        kodastest=a*1+b*2+c*3+d*4+e*5+f*6+g*7+h*8+i*9+j*1
        kodastest=int(kodastest)
        paskutinis=kodastest%11
        if paskutinis==10:
            kodastest2=a*3+b*4+c*5+d*6+e*7+f*8+g*9+h*1+i*2+j*3
            paskutinis=kodastest2%11
            if paskutinis==10:
                paskutinis=0
        kodukas=kodas1+str(paskutinis)
        kodukas=visi.append(kodukas)
        
    
    
    print(visi)
    print("Asmens kodų galimos kombinacijos:", len(visi))
    
    
    
