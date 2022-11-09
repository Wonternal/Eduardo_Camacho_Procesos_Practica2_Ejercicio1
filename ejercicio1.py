import os
from time import sleep

def padre():
    numHijos = int(input("Numero de procesos hijos que desea: "))
    for i in range(numHijos):
        newPid = os.fork()
        
        if newPid == 0:
            hijo()

        
def hijo():
    print(f"\n >>>>>>>>>>>>>>>>>>>>>> Soy el hijo con PID {os.getpid()}")
    sleep(5)
    print(f"\nSoy el hijo y voy a terminar. Mi PID {os.getpid()}")
    os._exit(0)
    
if __name__ == "__main__":
    padre()
