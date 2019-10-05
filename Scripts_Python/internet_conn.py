import requests

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

a = connected_to_internet()
print(a)

def telnet_test(ip, port):
    #if len(sys.argv) != 3:
    #    print("usage: telnet.py IPADDRESS PORT")
    #    exit(-1)

    print("Opening connection on %s port %s", ip, str(port))

    try:
        conn=socket.create_connection((ip,port),timeout=30)
    except socket.timeout:
        print("Connection error: timeout")
        exit(-1)
    except:
        print("Connection error: unknown")
        exit(-1)
    print("Connection succeed")
    exit(0)

telnet_test("127.0.0.1", 1433)