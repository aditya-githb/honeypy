# honeypy
ssh and web honeypot

A honeypot to capture IP addresses, usernames, passwords, and commands. Written in Python.


An RSA key must be generated for the SSH server host key by the following
`ssh-keygen -t rsa -b 2048 -f server.key`

# Usage
```
-a / --address: Bind address.
-p / --port: Port.
-s / --ssh OR -wh / --http: Declare honeypot type.
```

Example: `python3 honeypy.py -a 0.0.0.0 -p 22 --ssh`
