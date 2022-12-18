import random

participantes = open("participantes").readlines()
premios = open("premios").readlines()

resultados_sorteo = list()

for premio in premios:
    participante = random.choice(participantes)
    participantes.remove(participante)
    resultados_sorteo.append((participante,premio))

for resultado in resultados_sorteo:
    print(resultado[0] + resultado[1])
else:
    print("\n### Fin del sorteo ###")
