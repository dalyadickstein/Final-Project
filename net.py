import json
import socket

from contextlib import contextmanager

@contextmanager
def start_server_and_connect_to_client():
  # set up server
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', 0))
  server_socket.listen(1)
  
  # print host name and port number so client can connect
  print('Host: ' + socket.gethostname())
  print('Port: ' + str(server_socket.getsockname()[1]))

  # wait for client to connect
  client_socket = server_socket.accept()[0]
  yield client_socket
  
  # close our sockets
  client_socket.close()
  server_socket.close()

@contextmanager
def start_client_and_connect_to_server():
  host = input('Host: ')
  port = input('Port: ')
  client_socket = socket.create_connection((host, port))
  yield client_socket
  client_socket.close()

def send(peer_socket, data):
  msg = json.dumps(data).encode('utf-8')
  # # # # # # # # # # # # # # # # # # # 
  #                                   #
  #   ASK LEE ABOUT HTONL AND NTOHL   #
  #                                   #
  # # # # # # # # # # # # # # # # # # #
  msg_size = socket.htonl(len(msg)).to_bytes(4, byteorder='big')
  msg = msg_size + msg # prepend size of message to message body
  while msg:
    num_bytes_sent = peer_socket.send(msg)
    if num_bytes_sent == 0:
      raise SystemExit('connection terminated')
    msg = msg[num_bytes_sent:]

def receive(peer_socket):
  # read the first 4 bytes as integer to determine length of message
  msg_size = socket.ntohl(int.from_bytes(peer_socket.recv(4), byteorder='big'))
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
  msg = b''.join(msg_chunx).decode('utf-8')
  try:
    data = json.loads(msg) # message is string here
  except Exception as e:
    raise e
    data = { 'error_msg': 'Badly formed message', 'exception': e }
  return data
