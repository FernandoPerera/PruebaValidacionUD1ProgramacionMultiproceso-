import os
from datetime import datetime

from time import sleep

def father() :  
     
     contador = 1   
      
     while (contador <= 10) :
        
        newPid = os.fork()

        if newPid == 0 : 
            children()
        else :
            childrenPid = newPid
            date = datetime.now()
            print('\nIniciando el proceso : %d a las %s \n ' % (childrenPid, date.time().strftime("%H:%M:%S")))

            sleep(10) 
        contador += 1
def children() :
    
    print('\t········ | Iniciando proceso con PID %d | ········\n' % os.getpid())
    sleep(3)
    print('\n\t········ | Terminando el proceso con PID %d  | ········' % os.getpid())

    os._exit(0) 
    
father()
