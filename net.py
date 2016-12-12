import json
import socket

from contextlib import contextmanager

# technique mentioned on StackOverflow
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
def get_local_ipv4():
  # Try to get local IP that other computers can recognize you by
  ip = '127.0.0.1'
  try: 
    ip = socket.gethostbyname(socket.gethostname())
  except OSError:
    pass
  # If IP is only returning local host, try a different method
  if ip == '127.0.0.1' or ip == '0.0.0.0':
    # try to connect to Google DNS and check own address from connection
    temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
      temp.connect(('8.8.8.8', 53))
      ip = temp.getsockname()[0]
    except OSError:
      pass
    finally:
      temp.close()
  return ip

@contextmanager
def start_server_and_connect_to_client():
  # set up server
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', 0))
  server_socket.listen(1)
  
  # print host name and port number so client can connect
  print('Host: ' + get_local_ipv4())
  print('Port: ' + str(server_socket.getsockname()[1]))

  # wait for client to connect
  client_socket = server_socket.accept()[0]
  yield client_socket # code from game.py runs here before closing socket
  
  # close our sockets
  client_socket.close()
  server_socket.close()

@contextmanager
def start_client_and_connect_to_server():
  host = input('Host: ')
  port = input('Port: ')
  client_socket = socket.create_connection((host, port))
  yield client_socket # code from game.py runs here before closing socket
  client_socket.close()

def send(peer_socket, data):
  msg = json.dumps(data).encode('utf-8')
  msg_size = len(msg).to_bytes(4, byteorder='big')
  msg = msg_size + msg # prepend size of message to message body
  while msg:
    num_bytes_sent = peer_socket.send(msg)
    if num_bytes_sent == 0:
      raise SystemExit('connection terminated')
    msg = msg[num_bytes_sent:]

def receive(peer_socket):
  # read the first 4 bytes as integer to determine length of message
  msg_size = int.from_bytes(peer_socket.recv(4), byteorder='big')
  if msg_size == 0:
    raise SystemExit('connection terminated')
  msg_chunx = []
  num_bytes_received = 0
  while num_bytes_received < msg_size: # still have more to go
    msg_chunk = peer_socket.recv(msg_size - num_bytes_received)
    if len(msg_chunk) == 0:
      raise SystemExit('connection terminated')
    msg_chunx.append(msg_chunk)
    num_bytes_received += len(msg_chunk)
  return json.loads(b''.join(msg_chunx).decode('utf-8'))
