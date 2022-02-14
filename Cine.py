import threading
import time

class Cine():
    def __init__(self, lista = 0):
        self.locked = threading.Lock()
        self.list_send = lista
        
    def asignar_turno(self):
        self.locked.acquire()
        
        try: 
            
            self.list_send += 2
            print('Numero de personas:',self.list_send)
            print('turno :',self.list_send-1)
            print('Espera tu turno')
            time.sleep(5)
        finally:
            self.locked.release()
            
def Iniciar(x):
    
    for y in range(2):
        x.asignar_turno()
        
        
if __name__ == '__main__':
    cine = Cine()
    for y in range(2):
        print('Pasar de dos en dos')
        tstart = threading.Thread(target=Iniciar, args=(cine,))
        tstart.start()