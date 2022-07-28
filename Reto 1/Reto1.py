# Reto 1
# Lenguaje: Python
# IDE recomendado: PyCharm
# Nivel: Inicial
# Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
# Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls).

import pandas as pd

df = pd.read_excel('Reto1.xlsx')

mails = df['Email']

print('Cantidad inicial:',mails.size)

mails = df['Email'].drop_duplicates()

print('Cantidad final:',mails.size)

print('Mails unicos')
for mail in mails:
    print(mail)




