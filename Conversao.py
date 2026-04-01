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
