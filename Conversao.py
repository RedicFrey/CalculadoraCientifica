# import requests 

# # url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" &gt; 

# # def cotacao_dolar():
# #     response = requests.get(url) 
# #     if response.status_code == 200:
# #         data = response.json() 
       
# #         dolar = data["USDBRL"]["bid"]  
# #         return dolar
# #     else:
# #         return print("Erro ao buscar cotação")



# # # def Conversao():
# #     url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" &gt; 
# #     try:
# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             data = response.json()
# #             dolar = float(data["USDBRL"]["bid"])
            
# #             print(f"\nCotação atual do Dólar: R$ {dolar:.2f}")
# #             print("1. Dólar para Real\n2. Real para Dólar")
# #             tipo = int(input("Escolha: "))
            
# #             if tipo == 1:
# #                 v = float(input("Valor em US$: "))
# #                 return f"R$ {v * dolar:.2f}"
# #             else:
# #                 v = float(input("Valor em R$: "))
# #                 return f"US$ {v / dolar:.2f}"
# #         return "Erro na API"
# #     except:
# #         return "Erro de conexão"        



import requests

def Conversao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            dolar = float(data["USDBRL"]["bid"])
            
            print(f"\nCotação atual: R$ {dolar:.2f}")
            print("1. Converter Dólar para Real")
            print("2. Converter Real para Dólar")
            opcao = int(input("Escolha: "))
            
            if opcao == 1:
                valor = float(input("Valor em US$: "))
                return f"R$ {valor * dolar:.2f}"
            else:
                valor = float(input("Valor em R$: "))
                return f"US$ {valor / dolar:.2f}"
        else:
            return "Erro ao acessar API"
    except Exception as e:
        return f"Erro de conexão: {e}"