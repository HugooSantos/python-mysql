import mysql.connector

con = mysql.connector.connect(host='localhost',database='fazenda_bd',user='root',password='155155')
if con.is_connected():
     print('conectado ao servidor')
cursor = con.cursor()
cursor.execute("select id_rebanho from rebanho")
for x in cursor:
 print(x)



def readequação(txt):
    print('-' * 50)
    print(txt)
    print('-' * 50)


readequação('processo efetivo')
import random
volume = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
litros = 15
c = 1
for c in range(1, 8):
    extração = random.choice(volume)
    print(extração)
    if litros >= extração:
      print('>>>>>> volume dentro do permitido para produção <<<<<<')
    if litros < extração:
      print(' volume acima do permitido !!!!')
    if extração == 0:
      print('vaca ja ordenhada!')
    else:
      print('Fim de processo de extração!')
# busca binária


import math
def fazenda(txt):
 print('-' * 50)
 print(txt)
 print('-' * 50)



fazenda('fazentech')
vacas = [x]
n = 8
ordenhado = 2
report =(vacas, n, ordenhado)
print(report)
quant = len(vacas)
print(quant)
def busca_binaria(vacas, n, ordenhado):
 esquerda = 0,direita (n) - 1
 while esquerda <= direita:
     meio = ((esquerda + direita) / 2)
 if vacas[vacas] == ordenhado:
    return meio
 if vacas[meio] > ordenhado:
    direita = meio - 1
 else:
    esquerda = meio + 1
    return -1
