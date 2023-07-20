import threading
import socket
import random

quotes = ["The only true wisdom is knowing you know nothing - Socrates "]

def handle_socket(c):
    # Get the quote
    qotd = random.choice(quotes)

    # Send the quote to the client
    c.send(qotd.encode())
    print(qotd)

    # Close the connection
    c.close()

# create socket
s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888

# binding socket to port 8888
s.bind(('', port))
print ("Socket binded to " + str(port))

# Listen for connections
s.listen(5)
print ("Socket is listening")

# start a new thread for each connection
while True:
    # Accept a connection
    c, addr = s.accept()

    # create a new thread to handle connection
    thread = threading.Thread(target=handle_socket, args=(c,))
    thread.start()

