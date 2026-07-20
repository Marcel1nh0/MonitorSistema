import time
import psutil

def get_top_processes(n=5, interval=1.0):
    processos = list(psutil.process_iter(['pid', 'name']))


    for proc in processos:
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(interval)  

    dados = []
    for proc in processos:
        try:
            dados.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu': proc.cpu_percent(interval=None)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    dados.sort(key=lambda p: p['cpu'], reverse=True)
    return dados[:n]


# teste
DURACAO_TESTE = 15  
inicio = time.time()

while time.time() - inicio < DURACAO_TESTE:
    top5 = get_top_processes(n=5, interval=1.0)

    print("\033[H\033[J", end="")  # Pode causar problemas com terminais próprios de IDE use o do sistema mesmo
    print(f"Top 5 processos (rodando há {int(time.time() - inicio)}s):\n")
    for p in top5:
        print(f"PID {p['pid']:>6} | {p['name']:<25} | CPU: {p['cpu']:.1f}%")

print("\nTeste finalizado.")
