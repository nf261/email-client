from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # mailserver='smtp.nyu.edu'
    # port = 25

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # Fill in end

    # if recv[:3] != '220':
    #   print('220 reply not received from server.')
    # else:
    #    print(input("Socket established. " + recv))

    # Send HELO command and print server response.
    heloCommand = 'Helo Nasser\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # if recv[:3] != '250':
    #   print('250 reply not received from server.')
    # else:
    #   print(input("HELO is good. " + recv))

    # Send MAIL FROM command and print
    # server response.
    # Fill in start

    mailfromCommand = 'MAIL FROM:<nasser.fattah@gmail.com>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # if recv[:3] != '250':
    #   print('mail from 250 reply not received from server.')
    # else:
    #   print(input("Mail From is good. " + recv))
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO:<nf261@nyu.edu>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # if recv[:3] != '250':
    #   print('rcpt to 250 reply not received from server.')
    # else:
    #   print(input("Rcpt To is good. " + recv))
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)

    # if recv[:3] != '354':
    #   print('data 250 reply not received from server.')
    # else:
    #   print(input("Data is good. " + recv))
    # Fill in end

    # Send message data.
    # Fill in start

    # message = 'Message coming from SMTP client\r\n'
    clientSocket.send(msg.encode())

    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # if recv[:3] != '250':
    #   print('end msg 250 reply not received from server.')
    # else:
    #   print(input("Msg period is good. " + recv))
    # Fill in end


    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    # print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # if recv[:3] != '250':
    #   print('quit 250 reply not received from server.')

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
