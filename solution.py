from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    
    mailserver = '127.0.0.1'
    port = 1025
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    heloCommand = 'Helo\r\n'
    clientSocket.send(heloCommand.encode())

    mailfromCommand = 'MAIL FROM:<nasser.fattah@gmail.com>\r\n'
    clientSocket.send(mailfromCommand.encode())

    rcpttoCommand = 'RCPT TO:<nf261@nyu.edu>\r\n'
    clientSocket.send(rcpttoCommand.encode())

    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())

    clientSocket.send(msg.encode())

    clientSocket.send(endmsg.encode())

    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
