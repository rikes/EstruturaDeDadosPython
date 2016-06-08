from threading import Thread
import time

def my_function(i):
    print('Iniciando a Thread %d' % i)
    time.sleep(5)
    print('Fim da Thread %d ' % i)

for i in range(10):
    #Alvo e argumentos
    t = Thread(target = my_function, args = (i,))
    t.start()    