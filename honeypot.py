import argparse
from ssh_honeypot import *
from web_honeypot import * 

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--address', type=str, required=True, help="IP address to bind the honeypot")
    parser.add_argument('-p', '--port', type=int, required=True, help="Port to bind the honeypot")
    parser.add_argument('-u', '--username', type=str, help="Username for SSH authentication")
    parser.add_argument('-pw', '--password', type=str, help="Password for SSH authentication")

    parser.add_argument('-s', '--ssh', action="store_true", help="Run SSH honeypot")
    parser.add_argument('-w', '--http', action="store_true", help="Run HTTP honeypot")

    args = parser.parse_args()

    if not args.ssh and not args.http:
        parser.error("No honeypot type specified, add --ssh or --http")

    try:
        if args.ssh:
            print("[-] Running SSH HoneyPot....")
            honeypot(args.address, args.port, args.username, args.password)

            if not args.username:
                username = None
            if not args.password:
                password = None
        elif args.http:
            print("[-] Running HTTP WordPress HoneyPot....")

            if not args.username:
                username = "admin"
            if not args.password:
                password = "password"

            print(f"Port: {args.port} Username: {args.username} Password: {args.password}")
            run_web_honeypot(args.port, args.username, args.password)
    except Exception as e:
        print(f"\n Exiting HoneyPot due to an error: {e}\n")

if __name__ == "__main__":
    main()
