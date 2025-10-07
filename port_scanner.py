# port_scanner_v2.py

import socket
import argparse
import threading
from queue import Queue
from datetime import datetime
import time

# Dicionário de portas comuns para uma saída mais informativa
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy",
}

# Lock para sincronizar o print na tela e evitar texto bagunçado
print_lock = threading.Lock()
open_ports = []

def scan_port(target_ip, port):
    """
    Tenta se conectar a uma única porta e determina se está aberta.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout menor para acelerar a verificação de portas fechadas
        sock.settimeout(0.5) 
        result = sock.connect_ex((target_ip, port))
        sock.close()
        
        if result == 0:
            # Usa o lock para garantir que o print não será interrompido por outra thread
            with print_lock:
                service = COMMON_PORTS.get(port, "Desconhecido")
                print(f"[+] Porta {port} está aberta ({service})")
                open_ports.append(port)
    except socket.error as e:
        # Em caso de erro, apenas ignora
        pass

def worker(target_ip, port_queue):
    """
    Função que cada thread irá executar. Pega uma porta da fila e a escaneia.
    """
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(target_ip, port)
        port_queue.task_done()

def main():
    # --- Configuração dos Argumentos de Linha de Comando ---
    parser = argparse.ArgumentParser(description="Port Scanner Rápido com Multi-threading")
    parser.add_argument("alvo", help="O alvo a ser escaneado (IP ou domínio).")
    parser.add_argument("-i", "--inicio", type=int, default=1, help="Porta inicial do scan (padrão: 1).")
    parser.add_argument("-f", "--fim", type=int, default=1024, help="Porta final do scan (padrão: 1024).")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Número de threads a serem usadas (padrão: 100).")
    args = parser.parse_args()

    # --- Início do Scan ---
    print("-" * 50)
    print(f"Escaneando {args.alvo}")
    print(f"Intervalo de Portas: {args.inicio}-{args.fim}")
    print(f"Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    start_time = time.time()

    try:
        target_ip = socket.gethostbyname(args.alvo)
    except socket.gaierror:
        print(f"[ERRO] Não foi possível resolver o host: {args.alvo}")
        return

    port_queue = Queue()
    for port in range(args.inicio, args.fim + 1):
        port_queue.put(port)
    
    threads = []
    for _ in range(args.threads):
        thread = threading.Thread(target=worker, args=(target_ip, port_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # --- Fim do Scan e Resumo ---
    end_time = time.time()
    duration = end_time - start_time

    print("-" * 50)
    print("Varredura Concluída!")
    if open_ports:
        print("Resumo das portas abertas:")
        # Ordena as portas para uma exibição limpa
        for port in sorted(open_ports):
            service = COMMON_PORTS.get(port, "Desconhecido")
            print(f"  - Porta {port} ({service})")
    else:
        print("Nenhuma porta aberta foi encontrada no intervalo especificado.")
    
    print(f"\nDuração total: {duration:.2f} segundos")
    print("-" * 50)

if __name__ == "__main__":
    main()