import time

"""
print('-' * 50)
print(time.asctime())
print('-' * 50)
print(time.localtime())
"""

print('Giancarlo Haack Albano')

time.sleep(2) #em segundos

a = time.localtime()
print(a[3]) #pegando apenas a hora.. o localtime é uma lista com as informações detalhadas.

