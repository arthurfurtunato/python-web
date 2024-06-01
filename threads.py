import time
import concurrent.futures

# funções --> Corrotinas 
def consulta_dados(): # I/O Bound
  print("Consultando dados...")
  time.sleep(2) # Simula a consulta de dados
  return "dados"

def processa_dados(dados): # CPU Bound
  print("Processando dados...")
  time.sleep(2) # Simula o processamento de dados

def grava_log(): # I/O Bound
  print("Gravando log...")
  time.sleep(2)

def main():
  start = time.perf_counter()
  print("Inicio")

  with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(consulta_dados) # Esperando BD
    dados = future.result()
    executor.submit(processa_dados, dados) # processa_dados depende de dados / em fast api seria await

    executor.submit(grava_log)

  # executor run...


  print("Fim")
  finish = time.perf_counter()
  print(f"Tempo de execução: {round(finish - start, 2)} segundos")

main()