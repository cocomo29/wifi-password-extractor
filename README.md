# wifi-password-extractor
take note of the wifi passwords that your computer has connected to.

# Steps:
- Download/clone the repo
- Run [main.py](main.py) </br>
Thats it :)

# Note:
`main.py` only shows you the passwords of WiFis thats you have or had connected to.

This task can be achieved manually by following these steps:

- open cmd
- type `netsh wlan show profiles`
- type `netsh wlan show profile <name> key=clear` </br>

`main.py` goes through all of the profiles and automates the task of manually executing the above mentioned command again and again!
