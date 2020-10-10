from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    
    mailserver = '127.0.0.1'
    port = 1025
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    
    mailfromCommand = 'MAIL FROM:<nasser.fattah@gmail.com>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    
    rcpttoCommand = 'RCPT To:<nasser.fattah@gmail.com>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    
    dataCommand = 'Data\r\n'
    clientSocket.send(dataCommand.encode())
    
    clientSocket.send(msg.encode())
    
    clientSocket.send(endmsg.encode())
    
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
