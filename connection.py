#I want to create a script that allows me to check for connection status

#Useful libraries that I would be working with -->
import os
import sys
import time
import socket


#Declaring the connection status function
def status(target, port):
    time.sleep(2)
        #while True:
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((target, port))
        stat = True
    except:
        stat = False
        #raise ConnectionError("The connection got disconnected or never exited")
        sys.exit()
        #break
    finally:
        print(f"Stat: {stat}")
        return stat


if __name__ == "__main__":
    print("CONNECTION STATUS \n")

    #a = status()

    print("\nExecuted successfully!")