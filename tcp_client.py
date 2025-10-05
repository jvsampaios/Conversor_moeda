import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

moedas_suportadas = {
    "1": "Dólar Americano",
    "2": "Euro",
    "3": "Libra Esterlina",
    "4": "Franco Suíço",
    "5": "Peso Argentino"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Conectado ao servidor em {SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        valor = input("Digite o valor em R$: ")
        try:
            valor_float = float(valor)
            if valor_float > 0:
                break
            else:
                print("Por favor, digite um valor maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número válido em reais.")

    print("\nEscolha a moeda de destino:")
    for codigo, nome in moedas_suportadas.items():
        print(f"{codigo} - {nome}")

    while True:
        moeda = input("Digite o número correspondente à moeda de destino: ")
        if moeda in moedas_suportadas:
            print(f"Você escolheu: {moedas_suportadas[moeda]}")
            break
        else:
            print("Opção inválida. Digite um número entre 1 e 5.")

    mensagem = f"{valor},{moeda}"
    print(f"\nEnviando para o servidor: '{mensagem}'")
    
    client_socket.sendall(mensagem.encode())
    
    data = client_socket.recv(1024)
    
    print("\n--- Resposta do Servidor ---")
    print(data.decode())
    print("--------------------------\n")

print("Conexão fechada.")