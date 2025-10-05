import socket
import random

HOST = '127.0.0.1'
PORT = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"Servidor TCP escutando em {HOST}:{PORT}")

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
        cotacao = random.uniform(5.5, 6.5)
        valor_convertido = valor_real / cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "2":
        cotacao = random.uniform(6.5, 7.0)
        valor_convertido = valor_real / cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "3":
        cotacao = random.uniform(7.0, 7.5)
        valor_convertido = valor_real / cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "4":
        cotacao = random.uniform(6.5, 7.2)
        valor_convertido = valor_real / cotacao
        return valor_convertido, cotacao
    elif moeda.lower() == "5":
        cotacao = random.uniform(0.001, 0.008)
        valor_convertido = valor_real / cotacao
        return valor_convertido, cotacao
    else:
        return None, None

while True:
    conn, addr = server_socket.accept()
    
    with conn:
        print(f"Conectado com {addr}")
        
        data = conn.recv(1024)
        
        if not data:
            break
            
        mensagem = data.decode()
        print(f"Mensagem recebida: {mensagem}")

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
        
        conn.sendall(resposta.encode())