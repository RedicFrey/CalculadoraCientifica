import divisao as d
import multplicar  as m
import potencia as p
import raizquadrada as rq
import soma as sm
import subtrai as s

# def perguntarnumeros():
#    d = int(input("Qual o numero"))
#    return 
    

def calculadora():
    print("\n\nqual operação deseja fazer?\n1. Soma\n2. subtração\n3. multplicação\n4. divisão\n5. potencia\n6. raiz quadrada")
    print("\n")
    decisao = int(input("escreva\n"))
    
    if(decisao == 1):
        a = int(input("Qual o numero 1"))
        b = int(input("Qual o numero 2"))
        x = sm.somar(a, b)  
    elif(decisao == 2):
        b = int(input("Qual o numero 2\n"))
        x = s.sub(a. b)
    elif (decisao == 3):
        a = int(input("Qual o numero 1\n"))
        b = int(input("Qual o numero 2\n"))
        x = m.mult(a, b) 
    elif (decisao == 4):
        a = int(input("Qual o numero 1\n"))
        b = int(input("Qual o numero 2\n"))
        x = d.divi(a, b)
    elif (decisao == 5):
        a = int(input("Qual o numero 1\n"))
        b = int(input("Qual o numero 2\n"))  
        x = p.poten(a, b)
    elif(decisao == 6):
        a = int(input("Qual o numero 1\n"))
        x = rq.raiz(a)
    return (x)    


