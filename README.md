Esse projeto nasceu como forma de aprender Python na prática, saindo da teoria pura e mexendo com algo que interage de verdade com o sistema operacional. Como venho de uma base em C e Linux, a ideia foi usar esse contraste pra sentir na pele as diferenças de filosofia entre as linguagens: tipagem dinâmica, gerenciamento automático de memória, sintaxe mais enxuta e um ecossistema de bibliotecas prontas pra praticamente tudo.

Pontos que quero desenvolver com esse projeto:

Sintaxe e idiomatismos de Python: list comprehensions, dicionários, tratamento de exceções (try/except), funções com parâmetros default
Manipulação de tempo e loops de execução contínua, algo que já é familiar de C mas com abordagem diferente
Uso de bibliotecas de terceiros (psutil) pra abstrair chamadas de sistema que em C eu precisaria fazer via /proc ou syscalls diretas
Boas práticas de projeto Python: futuramente separar em módulos, usar argparse, e possivelmente empacotar com pip
Sobre a lib psutil

O projeto usa psutil, uma biblioteca multiplataforma que dá acesso a informações do sistema (processos, CPU, memória, disco, rede) sem precisar ler diretamente arquivos do /proc (Linux) ou usar APIs específicas de cada SO. Ela foi escolhida porque:

Abstrai diferenças entre Linux, Windows e macOS
Tem uma API simples e bem documentada
É o padrão de fato pra esse tipo de monitoramento em Python

No código atual, ela é usada para:

Listar todos os processos rodando (psutil.process_iter)
Medir o consumo de CPU de cada processo (proc.cpu_percent)
Tratar processos que terminam ou não têm permissão de acesso durante a coleta (NoSuchProcess, AccessDenied)
Como funciona
Lista todos os processos ativos
Faz uma primeira leitura de CPU (necessária porque cpu_percent mede a diferença entre duas chamadas)
Espera um intervalo definido
Faz a segunda leitura e calcula o percentual de uso de CPU de cada processo
Ordena os processos por consumo e exibe os top N no terminal, atualizando a cada ciclo
Como rodar
bash
pip install psutil
python monitor.py

O script roda por um período de teste definido em DURACAO_TESTE (atualmente 15 segundos), atualizando a lista dos 5 processos mais pesados a cada segundo.

Estado atual
 Fase 1: exibição de uso de CPU e RAM
 Fase 2: top processos por consumo de CPU
 Fase 3: em planejamento
Ideias de melhorias futuras
Interface gráfica (GUI): usar tkinter (nativo) ou uma lib mais moderna como PyQt/customtkinter pra sair do terminal puro e ter uma janela com gráficos de uso em tempo real
Dashboard de terminal mais rico: usar rich ou curses pra ter cores, barras de progresso e um layout mais profissional sem sair do CLI
Monitorar RAM, disco e rede por processo, não só CPU
Alertas configuráveis: threshold de CPU/RAM que dispara aviso sonoro ou visual
Histórico em arquivo: salvar os dados coletados em CSV ou SQLite pra gerar gráficos de uso ao longo do tempo depois (ex: com matplotlib)
Argumentos de linha de comando via argparse: permitir configurar intervalo, número de processos exibidos e duração direto na chamada do script, tipo python monitor.py --interval 5 --top 10
Modular o código: separar coleta de dados, exibição e configuração em arquivos/módulos diferentes conforme o projeto cresce
