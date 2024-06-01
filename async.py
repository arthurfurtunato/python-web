import time
import asyncio

# funções --> Corrotinas 
async def consulta_dados(): # I/O Bound
  print("Consultando dados...")
  await asyncio.sleep(2) # Simula a consulta de dados
  return "dados"

async def processa_dados(dados): # CPU Bound
  print("Processando dados...")
  await asyncio.sleep(2) # Simula o processamento de dados

async def grava_log(): # I/O Bound
  print("Gravando log...")
  await asyncio.sleep(2)

async def main():
  dados = asyncio.create_task(consulta_dados()) # Future/Promessa
  asyncio.create_task(processa_dados(await dados))
  asyncio.create_task(grava_log())




start = time.perf_counter()
print("Inicio")

asyncio.run(main()) # Eventloop


print("Fim")
finish = time.perf_counter()
print(f"Tempo de execução: {round(finish - start, 2)} segundos")