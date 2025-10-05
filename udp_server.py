import socket
import random

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

print(f"Servidor UDP escutando em {HOST}:{PORT}")

moedas_suportadas = {
    "1": "Dólar Americano",
    "2": "Euro",
    "3": "Libra Esterlina",
    "4": "Franco Suíço",
    "5": "Peso Argentino"
}

def calcular_conversao(valor_real, moeda):
    """Gera uma cotação aleatória e calcula o valor convertido."""
    if moeda.lower() == "1":
        cotacao = random.uniform(0.15, 0.20)
        valor_convertido = valor_real * cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "2":
        cotacao = random.uniform(0.10, 0.15)
        valor_convertido = valor_real * cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "3":
        cotacao = random.uniform(0.05, 0.10)
        valor_convertido = valor_real * cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "4":
        cotacao = random.uniform(0.01, 0.05)
        valor_convertido = valor_real * cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "5":
        cotacao = random.uniform(260.0, 270.0)
        valor_convertido = valor_real * cotacao
        return valor_convertido, cotacao
    else:
        return None, None

while True:
    data, addr = server_socket.recvfrom(1024)
    mensagem = data.decode()
    print(f"Mensagem recebida de {addr}: {mensagem}")
    
    try:
        valor_str, moeda = mensagem.split(',')
        valor_real = float(valor_str)
        
        valor_convertido, cotacao = calcular_conversao(valor_real, moeda)
        
        if valor_convertido is not None:
            nome_moeda = moedas_suportadas.get(moeda.lower(), "desconhecida")
            resposta = (f"R$ {valor_real:.2f} equivalem a "
                        f"$ {valor_convertido:.2f} ({nome_moeda}). "
                        f"Cotação: R$ {cotacao:.2f}")
        else:
            resposta = f"Erro: A moeda '{moeda}' não é suportada. Tente 'dolar' ou 'euro'."

    except ValueError:
        resposta = "Erro: Formato da mensagem inválido. Use: VALOR,MOEDA (ex: 10,dolar)"

    server_socket.sendto(resposta.encode(), addr)