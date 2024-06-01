import time

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
  dados = consulta_dados()
  processa_dados(dados)
  grava_log()
  print("Fim")
  finish = time.perf_counter()
  print(f"Tempo de execução: {round(finish - start, 2)} segundos")

main()