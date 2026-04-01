import divisao as d
import multplicar  as m
import potencia as p
import raizquadrada as rq
import soma as sm
import subtrai as s
import Conversao as c


# def perguntarnumeros():
#    d = int(input("Qual o numero"))
#    return 
    

def calculadora():
    print("\nQual operação deseja fazer?\n1. Soma\n2. subtração\n3. multplicação\n4. divisão\n5. potencia\n6. raiz quadrada\n7. Conversao")
    print("\n")
    while(True):
        decisao = int(input("escreva\n"))
        
        if(decisao == 1):
            a = int(input("Qual o numero 1\n"))
            b = int(input("Qual o numero 2\n"))
            x = sm.somar(a, b)  
            break
        elif(decisao == 2):
            a = int(input("Qual o numero 1\n")) 
            b = int(input("Qual o numero 2\n"))
            x = s.sub(a, b)
            break
        elif (decisao == 3):
            a = int(input("Qual o numero 1\n"))
            b = int(input("Qual o numero 2\n"))
            x = m.mult(a, b) 
            break
        elif (decisao == 4):
            a = int(input("Qual o numero 1\n"))
            b = int(input("Qual o numero 2\n"))
            x = d.divi(a, b)
            break
        elif (decisao == 5):
            a = int(input("Qual o numero 1\n"))
            b = int(input("Qual o numero 2\n"))  
            x = p.poten(a, b)
            break
        elif(decisao == 6):
            a = int(input("Qual o numero 1\n"))
            x = rq.raiz(a)
            break
        elif(decisao == 7):
            x = c.Conversao() 
            break
        else:
            print("opção invalida\n")
            continue       
    return (x)    



