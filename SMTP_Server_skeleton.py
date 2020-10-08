from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    mailserver='127.0.0.1'
    port = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # print(clientSocket)
    # print(input("above shows the socket for local and remote machines"))

    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
        # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Nasser\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # if recv1[:3] != '250':
        # print('250 reply not received from server.')
    # else:
        # print(input("HELO is good"))

    # Send MAIL FROM command and print
    # server response.
    # Fill in start

    mailfromCommand = 'MAIL FROM: <nf261@nyu.edu>\r\n.'
    clientSocket.send(mailfromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # if recv1[:3] != '250':
        # print('mail from 250 reply not received from server.')
    # else:
        # print(input("Mail From is good"))
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO: <hi@funny.com>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # if recv1[:3] != '250':
        # print('rcpt to 250 reply not received from server.')
    # else:
        # print(input("Rcpt tp is good"))
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'Data'
    print(dataCommand)
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    # if recv1[:3] != '250':
        # print('data 250 reply not received from server.')
    # else:
        # print(input("Data is good"))
    # Fill in end

    # Send message data.
    message = input("Enter what you want to send via email: ")
    # mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    # if recv1[:3] != '250':
        # print('end msg 250 reply not received from server.')
    # else:
        # print(input("Msg is good"))
    # Fill in start
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(mailMessageEnd.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)

    # if recv1[:3] != '250':
        # print('end msg 250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    # print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)

    # if recv1[:3] != '250':
        # print('quit 250 reply not received from server.')

        pass
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
